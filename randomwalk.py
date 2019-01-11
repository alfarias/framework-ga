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

class RandomWalk(object): # Classe onde há a implementação dos operadores genéticos.
# Deve usar cruzamento aritmético e mutação Gaussiana.
# A seleção deve ser por torneio.
# A troca da população será geracional.   
    
    def __init__(self, population, fitness, population_count):
        self.population = population
        self.fitness = fitness
        self.population_count = population_count
        
    def heap_sort(self, population_fitness, population_chromosome): # Função de Heap Sort para a ordenação da população
        index_final = len(population_fitness)-1
        half_population_fitness = int(index_final/2)
    
        for i in range(half_population_fitness, -1, -1):
            self.create_heap(population_fitness, population_chromosome, i, index_final)
    
        for i in range(index_final, 0, -1):
            if population_fitness[0] > population_fitness[i]:
                population_fitness[0], population_fitness[i] = population_fitness[i], population_fitness[0]
                population_chromosome[0], population_chromosome[i] = population_chromosome[i], population_chromosome[0]
                self.create_heap(population_fitness, population_chromosome, 0, i - 1)
        return population_fitness, population_chromosome


    def create_heap(self, population_fitness, population_chromosome, start, end): # Cria a arvore para o Heap Sort
        child = start * 2 + 1
        while child <= end:
            if (child < end) and (population_fitness[child] < population_fitness[child + 1]):
                child += 1
            if population_fitness[start] < population_fitness[child]:
                population_fitness[start], population_fitness[child] = population_fitness[child], population_fitness[start]
                population_chromosome[start], population_chromosome[child] = population_chromosome[child], population_chromosome[start]
                start = child
                child = 2 * start + 1
            else:
                return        
    
    def mutation(self, standard_deviation): # Realiza a Mutação Gaussiana
        mutated = np.absolute(random.gauss(np.round(self.population,5), standard_deviation))  
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
target_normalized = [round((float(target_word[i])-50)/(130-50),5) for i in range(target_word_len)] # Valor da Palavra-alvo normalizada
generations = int(data_file[15]) # Número de Gerações                               
attempt = 5 # Número de execuções                               
# Características do Cromossomo
chromosome_length = len(target_word) # Tamanho do individuo a ser repassado como argumento para a geração da população
chromosome_min = 0 # Valor minimo de um gene do cromossomo
chromosome_max = 1 # Valor máximo de um gene do cromossomo
individual_min = 50 # Valor minimo de um gene do indivíduo
individual_max = 130 # Valor máximo de um gene do indivíduo

# Função Principal
best_fit_attempt = []
best_attempt = []
population_fitness = []
for i in range(attempt): # Inicio das 5 execuções
    population = GeneratePopulation(population_count)
    population_chromosome = population.create_population(chromosome_length,chromosome_max,chromosome_min)
    fitness = Evaluate(target_word)
    for i in range (population_count):
        population_fitness.append(fitness.calculate_fitness(population_chromosome[i], individual_max, individual_min))
    best_fit_gen = []
#    best = 0
#    best_fitness = 0
    for i in range(generations): # Inicio das Execuções por Geração
        rw = RandomWalk(population_chromosome, population_fitness, population_count) # Instanciamento da Classe GeneticAlgorithm
        population_fitness, population_chromosome = rw.heap_sort(population_fitness, population_chromosome)# Ordenação da População
        population_chromosome.reverse()
        population_fitness.reverse()
        offspring = rw.mutation(standard_deviation) # Mutação Gaussiana
        
        offspring_fitness = []
        for i in range (population_count):
            offspring_fitness.append(fitness.calculate_fitness(offspring[i], individual_max, individual_min))
        
        for i in range(len(population_fitness)):
            if offspring_fitness[i] > population_fitness[i]:
                population_chromosome[i] = offspring[i]
                population_fitness[i] = offspring_fitness[i]
            else:
                pass
        # Ordenação da população
        population_fitness, population_chromosome = rw.heap_sort(population_fitness, population_chromosome)
        population_chromosome.reverse()
        population_fitness.reverse()
        
        # Remoção de 10% da nova população
        pop_ten_pc = (population_count*10)/100
        pop_removed = int(pop_ten_pc)
        population_chromosome = population_chromosome[:-pop_removed]
        population_fitness = population_fitness[:-pop_removed]
        
        # Inclusão de novos Cromossomos a população gerada
        new_chromosome = Chromosome(chromosome_length, chromosome_max, chromosome_min)
        new_fitness = Evaluate(target_word)
        population_new = [new_chromosome.create_chromosome() for x in range(pop_removed)]
        population_chromosome = population_chromosome + population_new
        population_new_fitness = []
        for i in range (pop_removed):
            population_new_fitness.append(new_fitness.calculate_fitness(population_new[i], individual_max, individual_min))
        population_fitness = population_fitness + population_new_fitness
        best_fit_gen.append(population_fitness[0])
    best_fit_attempt.append(best_fit_gen)
    best_attempt.append(population_chromosome[0])
    population_fitness = []
    
best_attempt_desnorm = []
best_des = Evaluate(target_word)
for i in range (attempt):
    best_attempt_desnorm.append(best_des.desnormalize(best_attempt[i], individual_max, individual_min)) 

# Salva os resultados em arquivos .csv

with open('rw_elite_fit_gen.csv','w') as outfile:
    best_fit_gen_data = csv.writer(outfile)
    best_fit_gen_data.writerow(best_fit_gen)
    
with open('rw_elite_fit_attempt.csv','w') as outfile:
    best_fit_attempt_data = csv.writer(outfile)
    for row in best_fit_attempt:
        best_fit_attempt_data.writerow(row)

with open('rw_elite_attempt.csv','w') as outfile:
    best_attempt_data = csv.writer(outfile)
    for row in best_attempt:
        best_attempt_data.writerow(row)     
        
with open('rw_elite_attempt_desnorm.csv','w') as outfile:
    best_attempt_desnorm_data = csv.writer(outfile)
    for row in best_attempt_desnorm:
        best_attempt_desnorm_data.writerow(row) 