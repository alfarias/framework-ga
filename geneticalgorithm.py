"""" 

                  Trabalho de Computação Evolucionária

Será criado a primeira versão do AG e seu desempenho será comparado a um random walk para a tarefa de encontrar um palavra de número reais.
Fazer o diagrama UML do projeto.
Uma apresentação sobre o seu AG que vai sendo atualizada ao longo do curso.
Lembre que cada algoritmo deve ser executado 5 vezes e seus gráficos serem feitos em cima das suas estatísticas: média e desvio padrão.
Deve ser mostrado o número de acertos médios da palavra, e a avaliação da acurácia e precisão do algoritmo (ver slide Gráficos).
Uso do Mersenne Twister para a geração de números aleatórios.
(Python já usa por padrão este algoritmo na biblioteca random. Fonte: https://docs.python.org/2/library/random.html)

@author: Farb

"""

import random
from random import randint 
import numpy as np
import csv

class GetConfigFile(object):
    def __init__(self, file):
        self.file = file
        
   
    def read_file(self): # Função que realiza a leitura do arquivo de texto linha por linha
        with open(self.file) as f:
            content = f.read().splitlines()
        return content

class Chromosome(object): # Classe onde o Cromossomo é gerado.
    def __init__(self, length, max, min):
        self.length = length
        self.max = max
        self.min = min
        
    def create_chromosome(self):
        return [round(random.uniform(self.min,self.max),5) for x in range(self.length)]

class GeneratePopulation(object): # Classe onde a população é gerada.
    def __init__(self, count):
        self.count = count
        
    def create_population(self, length, max, min):
        chromosome = Chromosome(length, max, min) # Instaciamento
        return [chromosome.create_chromosome() for x in range(self.count)]
        
class Evaluate(object):
# A classe avaliador é a interface do AG com o problema que está sendo otimizado. 
# Nesta classe o cromossomo é decodificado para gerar o individuo, do qual é calculado o fitness.
    def __init__(self, target):
        self.target = target

    def desnormalize(self, chromosome, max, min):
        chromosome_len = len(chromosome)
        a = [round(float(chromosome[i])*(max-min)+(min),3) for i in range(chromosome_len)]
        return a
        
    def calculate_fitness(self, chromosome, max, min): # O cálculo é baseado no inverso da distância entre o indivíduo e a Palavra-Alvo
        individual = self.desnormalize(chromosome, max, min)
        distance = np.absolute(np.array(self.target) - np.array(individual)) # Calcula a distância entre a palavra-alvo e o indivíduo.
        return (1/(sum(distance)+0.1)) # Valor do Fitness com a ideia de maximização. Fitness máximo = 1000.0

class GeneticAlgorithm(object): # Classe onde há a implementação dos operadores genéticos.
# Deve usar cruzamento aritmético e mutação Gaussiana.
# A seleção deve ser por torneio.
# A troca da população será geracional.   
    
    def __init__(self, population, fitness, population_count):
        self.population = population
        self.fitness = fitness
        self.population_count = population_count
    
    def selection(self, ring_size): # Seleção por Torneio.
        selected_winners = []
        for x in range(len(self.population)):
            selected = [randint(0,len(self.population) - 1) for i in range(ring_size)]
            aux = self.fitness[selected[0]]
            index = selected[0]
            for i in range(1,ring_size-1):
                if self.fitness[selected[i]] >= aux:
                    aux = self.fitness[selected[i]]
                    index = selected[i]
            selected_winners.append(self.population[index])
        return selected_winners
    
    def crossover(self, selected_winners, crossover_probability): # Cruzamento Aritmético.
        offspring = []
        i = 0          
        while i < (int(self.population_count/2)):
            chance = random.random()
            alpha = random.random()
            # Coeficiente aleatório de 0 a 1 para o cálculo do cruzamento aritmético
            if chance <= crossover_probability:
                parent_a = np.array(random.choice(selected_winners))
                parent_b = np.array(random.choice(selected_winners))
            else:
                continue
            if parent_a is not parent_b:
                offspring_a = np.round(parent_a + (parent_b - parent_a)*alpha,5) # Cruzamento aritmético
                offspring_b = np.round(parent_b + (parent_a - parent_b)*alpha,5) # Cruzamento aritmético
                i = i+1
            else:
                continue        
            offspring.append(offspring_a.tolist()) 
            offspring.append(offspring_b.tolist())

        return offspring
    
    def mutation(self, offspring, standard_deviation,mutation_probability): # Falta adicionar mutation_probability aos argumentos
        mutated = [[np.absolute(random.gauss(gene, standard_deviation)) if random.random() <= mutation_probability else gene for gene in sublst] for sublst in offspring]  
        new_mut = [[1-(abs(gene-1)) if gene > 1 else gene for gene in sublst] for sublst in mutated]
        new_mut_round = np.round(new_mut,5)
        new_mut_final = new_mut_round.tolist()
        return new_mut_final
    
    def get_best_fitness(self, offspring, offspring_fitness): # Pega o melhor fitnessa da população
        best_offspring_fitness = offspring_fitness[0]
        best_offspring = offspring[0]
        for i in range(1, self.population_count):
            if offspring_fitness[i] > best_offspring_fitness:
                best_offspring_fitness = offspring_fitness[i]
                best_offspring = offspring[i]
        return best_offspring_fitness, best_offspring    
    
    
    def elitism(self, offspring, offspring_fitness, elite, elite_fitness): # Realiza o Elitismo

        best_offspring_fitness, best_offspring = self.get_best_fitness(offspring, offspring_fitness)
        
        if best_offspring_fitness < elite_fitness:
            i = randint(0,population_count-1)
            offspring[i] = elite
            offspring_fitness[i] = elite_fitness
        if best_offspring_fitness > elite_fitness:
            elite_fitness = best_offspring_fitness
            elite = best_offspring
        else:
            pass
        return offspring, offspring_fitness, elite, elite_fitness
	# Caso seja necessário, declarar outros métodos dentro da Classe GeneticAlgorithm.


# Leitura dos parâmetros contidos no arquivo txt
data = GetConfigFile('parameters.txt')
data_file = data.read_file() # Realiza a leitura do arquivo de configuração
population_count = int(data_file[1]) # Tamanho da População - Linha 2
ring_size = int(data_file[3]) # Tamanho do Ring - Linha 4
crossover_probability = float(data_file[5]) # Probabilidade de Crossover - Linha 6
mutation_probability = float(data_file[7]) # Probabilidade de Mutação - Linha 8
standard_deviation = float(data_file[9]) # Desvio-Padrão (Mutação Gaussiana) - Linha 10
target_word_raw = data_file[11].split(",") # Palavra-Alvo - Linha 12
target_word_conv = list(map(float, target_word_raw)) # Palavra-Alvo em formato de lista
target_word = target_word_conv[:int(data_file[13])] # Pega os X primeiros valores da palavra-alvo
target_word_len = len(target_word)
target_normalized = [round((float(target_word[i])-50)/(130-50),5) for i in range(target_word_len)]
generations = int(data_file[15]) # Número de Gerações                               
attempt = 5 # Número de execuções                               
# Características do Cromossomo
chromosome_length = len(target_word) # Tamanho do individuo a ser repassado como argumento para a geração da população
chromosome_min = 0 # Valor minimo de um gene do cromossomo
chromosome_max = 1 # Valor máximo de um gene do cromossomo
individual_min = 50 # Valor minimo de um gene do indivíduo
individual_max = 130 # Valor máximo de um gene do indivíduo

# Função Principal
elite_fit_attempt = []
elite_attempt = []
for i in range(attempt):
    population = GeneratePopulation(population_count)
    population_chromosome = population.create_population(chromosome_length,chromosome_max,chromosome_min)
    fitness = Evaluate(target_word)
    population_fitness = []
    for i in range (population_count):
        population_fitness.append(fitness.calculate_fitness(population_chromosome[i], individual_max, individual_min))
    elite_fit_gen = []
    elite = 0
    elite_fitness = 0
    for i in range(generations):
        ga = GeneticAlgorithm(population_chromosome, population_fitness, population_count) # Instanciamento da Classe GeneticAlgorithm
        selected = ga.selection(ring_size) # Seleção por Torneio
        offspring = ga.crossover(selected, crossover_probability) # Cruzamento Aritmético
        offspring_mutated = ga.mutation(offspring, standard_deviation, mutation_probability) # Mutação Gaussiana
        
        offspring_fitness = []
        for i in range (population_count):
            offspring_fitness.append(fitness.calculate_fitness(offspring_mutated[i], individual_max, individual_min))
        
        offspring, offspring_fitness, elite, elite_fitness = ga.elitism(offspring_mutated, offspring_fitness, elite, elite_fitness)
        
        population_chromosome = offspring
        population_fitness = offspring_fitness
        elite_fit_gen.append(elite_fitness)
    elite_fit_attempt.append(elite_fit_gen)
    elite_attempt.append(elite)

elite_attempt_desnorm = []
elite_des = Evaluate(target_word)
for i in range (attempt):
    elite_attempt_desnorm.append(elite_des.desnormalize(elite_attempt[i], individual_max, individual_min))        

# Salva os resultados em arquivos .csv
with open('target_normalized.csv','w') as outfile:
    target_normalized_data = csv.writer(outfile)
    target_normalized_data.writerow(target_normalized)
    
with open('target_word.csv','w') as outfile:
    target_word_data = csv.writer(outfile)
    target_word_data.writerow(target_word)    

with open('ga_elite_fit_gen.csv','w') as outfile:
    elite_fit_gen_data = csv.writer(outfile)
    elite_fit_gen_data.writerow(elite_fit_gen)
    
with open('ga_elite_fit_attempt.csv','w') as outfile:
    elite_fit_attempt_data = csv.writer(outfile)
    for row in elite_fit_attempt:
        elite_fit_attempt_data.writerow(row)

with open('ga_elite_attempt.csv','w') as outfile:
    elite_attempt_data = csv.writer(outfile)
    for row in elite_attempt:
        elite_attempt_data.writerow(row)
        
with open('ga_elite_attempt_desnorm.csv','w') as outfile:
    elite_attempt_desnorm_data = csv.writer(outfile)
    for row in elite_attempt_desnorm:
        elite_attempt_desnorm_data.writerow(row) 