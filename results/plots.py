import matplotlib.pyplot as plt
import csv
import numpy as np

m1 = 10
m2 = 20
m3 = 30
n1 = 3000
n2 = 4000
n3 = 6000
attempt = 5

# Armazena os valores normalizados da palavra-alvo
with open('target_word_10.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    target_normalized_data_10 = []
    for p in range(0, m1):
        target_normalized_data_10.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            target_normalized_data_10[var_indice] = float(valor)
            var_indice += 1

with open('target_word_20.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    target_normalized_data_20 = []
    for p in range(0, m2):
        target_normalized_data_20.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            target_normalized_data_20[var_indice] = float(valor)
            var_indice += 1

with open('target_word_30.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    target_normalized_data_30 = []
    for p in range(0, m3):
        target_normalized_data_30.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            target_normalized_data_30[var_indice] = float(valor)
            var_indice += 1

# Dados do AG            
with open('ga_elite_fit_gen_10_50.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_gen_10_50 = []
    for p in range(0, n1):
        ga_elite_fit_gen_10_50.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            ga_elite_fit_gen_10_50[var_indice] = float(valor)
            var_indice += 1
            
with open('ga_elite_fit_attempt_10_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_attempt_10_50 = np.zeros((attempt,n1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_fit_attempt_10_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('ga_elite_attempt_desnorm_10_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_attempt_10_50 = np.zeros((attempt,m1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_attempt_10_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('ga_elite_fit_gen_20_50.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_gen_20_50 = []
    for p in range(0, n2):
        ga_elite_fit_gen_20_50.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            ga_elite_fit_gen_20_50[var_indice] = float(valor)
            var_indice += 1
            
with open('ga_elite_fit_attempt_20_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_attempt_20_50 = np.zeros((attempt,n2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_fit_attempt_20_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('ga_elite_attempt_desnorm_20_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_attempt_20_50 = np.zeros((attempt,m2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_attempt_20_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('ga_elite_fit_gen_30_50.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_gen_30_50 = []
    for p in range(0, n3):
        ga_elite_fit_gen_30_50.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            ga_elite_fit_gen_30_50[var_indice] = float(valor)
            var_indice += 1
            
with open('ga_elite_fit_attempt_30_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_attempt_30_50 = np.zeros((attempt,n3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_fit_attempt_30_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('ga_elite_attempt_desnorm_30_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_attempt_30_50 = np.zeros((attempt,m3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_attempt_30_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
 
with open('ga_elite_fit_gen_10_100.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_gen_10_100 = []
    for p in range(0, n1):
        ga_elite_fit_gen_10_100.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            ga_elite_fit_gen_10_100[var_indice] = float(valor)
            var_indice += 1
            
with open('ga_elite_fit_attempt_10_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_attempt_10_100 = np.zeros((attempt,n1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_fit_attempt_10_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('ga_elite_attempt_desnorm_10_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_attempt_10_100 = np.zeros((attempt,m1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_attempt_10_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('ga_elite_fit_gen_20_100.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_gen_20_100 = []
    for p in range(0, n2):
        ga_elite_fit_gen_20_100.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            ga_elite_fit_gen_20_100[var_indice] = float(valor)
            var_indice += 1
            
with open('ga_elite_fit_attempt_20_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_attempt_20_100 = np.zeros((attempt,n2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_fit_attempt_20_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('ga_elite_attempt_desnorm_20_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_attempt_20_100 = np.zeros((attempt,m2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_attempt_20_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('ga_elite_fit_gen_30_100.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_gen_30_100 = []
    for p in range(0, n3):
        ga_elite_fit_gen_30_100.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            ga_elite_fit_gen_30_100[var_indice] = float(valor)
            var_indice += 1
            
with open('ga_elite_fit_attempt_30_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_fit_attempt_30_100 = np.zeros((attempt,n3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_fit_attempt_30_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('ga_elite_attempt_desnorm_30_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    ga_elite_attempt_30_100 = np.zeros((attempt,m3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                ga_elite_attempt_30_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

          
# Dados do Random Walk
            
with open('rw_elite_fit_gen_10_50.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_gen_10_50 = []
    for p in range(0, n1):
        rw_elite_fit_gen_10_50.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            rw_elite_fit_gen_10_50[var_indice] = float(valor)
            var_indice += 1
            
with open('rw_elite_fit_attempt_10_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_attempt_10_50 = np.zeros((attempt,n1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_fit_attempt_10_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('rw_elite_attempt_desnorm_10_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_attempt_10_50 = np.zeros((attempt,m1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_attempt_10_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('rw_elite_fit_gen_20_50.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_gen_20_50 = []
    for p in range(0, n2):
        rw_elite_fit_gen_20_50.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            rw_elite_fit_gen_20_50[var_indice] = float(valor)
            var_indice += 1
            
with open('rw_elite_fit_attempt_20_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_attempt_20_50 = np.zeros((attempt,n2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_fit_attempt_20_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('rw_elite_attempt_desnorm_20_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_attempt_20_50 = np.zeros((attempt,m2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_attempt_20_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('rw_elite_fit_gen_30_50.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_gen_30_50 = []
    for p in range(0, n3):
        rw_elite_fit_gen_30_50.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            rw_elite_fit_gen_30_50[var_indice] = float(valor)
            var_indice += 1
            
with open('rw_elite_fit_attempt_30_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_attempt_30_50 = np.zeros((attempt,n3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_fit_attempt_30_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('rw_elite_attempt_desnorm_30_50.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_attempt_30_50 = np.zeros((attempt,m3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_attempt_30_50[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
 
with open('rw_elite_fit_gen_10_100.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_gen_10_100 = []
    for p in range(0, n1):
        rw_elite_fit_gen_10_100.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            rw_elite_fit_gen_10_100[var_indice] = float(valor)
            var_indice += 1
            
with open('rw_elite_fit_attempt_10_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_attempt_10_100 = np.zeros((attempt,n1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_fit_attempt_10_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('rw_elite_attempt_desnorm_10_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_attempt_10_100 = np.zeros((attempt,m1))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_attempt_10_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('rw_elite_fit_gen_20_100.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_gen_20_100 = []
    for p in range(0, n2):
        rw_elite_fit_gen_20_100.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            rw_elite_fit_gen_20_100[var_indice] = float(valor)
            var_indice += 1
            
with open('rw_elite_fit_attempt_20_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_attempt_20_100 = np.zeros((attempt,n2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_fit_attempt_20_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('rw_elite_attempt_desnorm_20_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_attempt_20_100 = np.zeros((attempt,m2))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_attempt_20_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1

with open('rw_elite_fit_gen_30_100.csv', 'r') as arq:
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_gen_30_100 = []
    for p in range(0, n3):
        rw_elite_fit_gen_30_100.append(0)
    for linha in reader:
        var_indice = 0
        for valor in linha:
            rw_elite_fit_gen_30_100[var_indice] = float(valor)
            var_indice += 1
            
with open('rw_elite_fit_attempt_30_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_fit_attempt_30_100 = np.zeros((attempt,n3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_fit_attempt_30_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1
            
with open('rw_elite_attempt_desnorm_30_100.csv', 'r') as arq:
    index_row = 0
    reader = csv.reader(arq, delimiter=',')
    rw_elite_attempt_30_100 = np.zeros((attempt,m3))
    for linha in reader:
        var_indice = 0
#        print(linha)
        if linha != []:
            for valor in linha:
                rw_elite_attempt_30_100[index_row][var_indice] = float(valor)
                var_indice += 1
            index_row +=1


def desv_padrao(matriz, media):
    x = len(matriz)
    y = len(matriz[0])
    soma_desvio = np.zeros(y)
    for i in range(0,x):
        va = 0
        for j in range(0,y):
            soma_desvio[va] += ((matriz[i][j] - media[va]) ** 2)
            va += 1
    for indice in range(0, len(soma_desvio)):
        soma_desvio[indice] /= 5
    desvio_padrao = np.sqrt(soma_desvio)
    return desvio_padrao

# Plots
# Parte 1

ga_elite_fit_attempt_mean_10_50 = np.mean(ga_elite_fit_attempt_10_50, axis=0)
rw_elite_fit_attempt_mean_10_50 = np.mean(rw_elite_fit_attempt_10_50, axis=0)
ga_elite_fit_attempt_std_10_50 = np.std(ga_elite_fit_attempt_10_50, axis=0)
rw_elite_fit_attempt_std_10_50 = np.std(rw_elite_fit_attempt_10_50, axis=0)

ga_elite_fit_attempt_mean_20_50 = np.mean(ga_elite_fit_attempt_20_50, axis=0)
rw_elite_fit_attempt_mean_20_50 = np.mean(rw_elite_fit_attempt_20_50, axis=0)
ga_elite_fit_attempt_std_20_50 = np.std(ga_elite_fit_attempt_20_50, axis=0)
rw_elite_fit_attempt_std_20_50 = np.std(rw_elite_fit_attempt_20_50, axis=0)

ga_elite_fit_attempt_mean_30_50 = np.mean(ga_elite_fit_attempt_30_50, axis=0)
rw_elite_fit_attempt_mean_30_50 = np.mean(rw_elite_fit_attempt_30_50, axis=0)
ga_elite_fit_attempt_std_30_50 = np.std(ga_elite_fit_attempt_30_50, axis=0)
rw_elite_fit_attempt_std_30_50 = np.std(rw_elite_fit_attempt_30_50, axis=0)

ga_elite_fit_attempt_mean_10_100 = np.mean(ga_elite_fit_attempt_10_100, axis=0)
rw_elite_fit_attempt_mean_10_100 = np.mean(rw_elite_fit_attempt_10_100, axis=0)
ga_elite_fit_attempt_std_10_100 = np.std(ga_elite_fit_attempt_10_100, axis=0)
rw_elite_fit_attempt_std_10_100 = np.std(rw_elite_fit_attempt_10_100, axis=0)

ga_elite_fit_attempt_mean_20_100 = np.mean(ga_elite_fit_attempt_20_100, axis=0)
rw_elite_fit_attempt_mean_20_100 = np.mean(rw_elite_fit_attempt_20_100, axis=0)
ga_elite_fit_attempt_std_20_100 = np.std(ga_elite_fit_attempt_20_100, axis=0)
rw_elite_fit_attempt_std_20_100 = np.std(rw_elite_fit_attempt_20_100, axis=0)

ga_elite_fit_attempt_mean_30_100 = np.mean(ga_elite_fit_attempt_30_100, axis=0)
rw_elite_fit_attempt_mean_30_100 = np.mean(rw_elite_fit_attempt_30_100, axis=0)
ga_elite_fit_attempt_std_30_100 = np.std(ga_elite_fit_attempt_30_100, axis=0)
rw_elite_fit_attempt_std_30_100 = np.std(rw_elite_fit_attempt_30_100, axis=0)

# Plots para População 50
fig = plt.figure()
plt.subplot(1, 1, 1)
fig.suptitle('Média e Desvio Padrão do Fitness por Geração (Palavra 10, População 50)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n1-1,n1)
plt.xlim((0,n1))
plt.errorbar(x,ga_elite_fit_attempt_mean_10_50,yerr=ga_elite_fit_attempt_std_10_50,errorevery=50,label="AG")
plt.subplot(1, 1, 1)
plt.errorbar(x,rw_elite_fit_attempt_mean_10_50,yerr=rw_elite_fit_attempt_std_10_50,errorevery=50,label="RW")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


fig = plt.figure()
fig.suptitle('Média e Desvio Padrão do Fitness por Geração no Random Walk (Palavra 10, População 50)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n1-1,n1)
plt.xlim((0,n1))
plt.errorbar(x,rw_elite_fit_attempt_mean_10_50,yerr=rw_elite_fit_attempt_std_10_50,errorevery=50,label="RW")
plt.show()

fig = plt.figure()
plt.subplot(1, 1, 1)
fig.suptitle('Média e Desvio Padrão do Fitness por Geração (Palavra 20, População 50)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n2-1,n2)
plt.xlim((0,n2))
plt.errorbar(x,ga_elite_fit_attempt_mean_20_50,yerr=ga_elite_fit_attempt_std_20_50,errorevery=50,label="AG")
plt.subplot(1, 1, 1)
plt.errorbar(x,rw_elite_fit_attempt_mean_20_50,yerr=rw_elite_fit_attempt_std_20_50,errorevery=50,label="RW")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

fig = plt.figure()
fig.suptitle('Média e Desvio Padrão do Fitness por Geração no Random Walk (Palavra 20, População 50)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n2-1,n2)
plt.xlim((0,n2))
plt.errorbar(x,rw_elite_fit_attempt_mean_20_50,yerr=rw_elite_fit_attempt_std_20_50,errorevery=50)
plt.show()

fig = plt.figure()
plt.subplot(1, 1, 1)
fig.suptitle('Média e Desvio Padrão do Fitness por Geração (Palavra 30, População 50)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n3-1,n3)
plt.xlim((0,n3))
plt.errorbar(x,ga_elite_fit_attempt_mean_30_50,yerr=ga_elite_fit_attempt_std_30_50,errorevery=50,label="AG")
plt.subplot(1, 1, 1)
plt.errorbar(x,rw_elite_fit_attempt_mean_30_50,yerr=rw_elite_fit_attempt_std_30_50,errorevery=50,label="RW")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

fig = plt.figure()
fig.suptitle('Média e Desvio Padrão do Fitness por Geração no Random Walk (Palavra 30, População 50)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n3-1,n3)
plt.xlim((0,n3))
plt.errorbar(x,rw_elite_fit_attempt_mean_30_50,yerr=rw_elite_fit_attempt_std_30_50,errorevery=50)
plt.show()

# Plots para População 100
fig = plt.figure()
plt.subplot(1, 1, 1)
fig.suptitle('Média e Desvio Padrão do Fitness por Geração (Palavra 10, População 100)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n1-1,n1)
plt.xlim((0,n1))
plt.errorbar(x,ga_elite_fit_attempt_mean_10_100,yerr=ga_elite_fit_attempt_std_10_100,errorevery=50,label="AG")
plt.subplot(1, 1, 1)
plt.errorbar(x,rw_elite_fit_attempt_mean_10_100,yerr=rw_elite_fit_attempt_std_10_100,errorevery=50,label="RW")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

fig = plt.figure()
fig.suptitle('Média e Desvio Padrão do Fitness por Geração no Random Walk (Palavra 10, População 100)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n1-1,n1)
plt.xlim((0,n1))
plt.errorbar(x,rw_elite_fit_attempt_mean_10_100,yerr=rw_elite_fit_attempt_std_10_100,errorevery=50,label="RW")
plt.show()

fig = plt.figure()
plt.subplot(1, 1, 1)
fig.suptitle('Média e Desvio Padrão do Fitness por Geração (Palavra 20, População 100)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n2-1,n2)
plt.xlim((0,n2))
plt.errorbar(x,ga_elite_fit_attempt_mean_20_100,yerr=ga_elite_fit_attempt_std_20_100,errorevery=50,label="AG")
plt.subplot(1, 1, 1)
plt.errorbar(x,rw_elite_fit_attempt_mean_20_100,yerr=rw_elite_fit_attempt_std_20_100,errorevery=50,label="RW")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

fig = plt.figure()
fig.suptitle('Média e Desvio Padrão do Fitness por Geração no Random Walk (Palavra 20, População 100)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n2-1,n2)
plt.xlim((0,n2))
plt.errorbar(x,rw_elite_fit_attempt_mean_20_100,yerr=rw_elite_fit_attempt_std_20_100,errorevery=50)
plt.show()

fig = plt.figure()
plt.subplot(1, 1, 1)
fig.suptitle('Média e Desvio Padrão do Fitness por Geração (Palavra 30, População 100)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n3-1,n3)
plt.xlim((0,n3))
plt.errorbar(x,ga_elite_fit_attempt_mean_30_100,yerr=ga_elite_fit_attempt_std_30_100,errorevery=50,label="AG")
plt.subplot(1, 1, 1)
plt.errorbar(x,rw_elite_fit_attempt_mean_30_100,yerr=rw_elite_fit_attempt_std_30_100,errorevery=50,label="RW")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

fig = plt.figure()
fig.suptitle('Média e Desvio Padrão do Fitness por Geração no Random Walk (Palavra 30, População 100)')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
x = np.linspace(0,n3-1,n3)
plt.xlim((0,n3))
plt.errorbar(x,rw_elite_fit_attempt_mean_30_100,yerr=rw_elite_fit_attempt_std_30_100,errorevery=50)
plt.show()

# Parte 2

ga_elite_attempt_std_10_50 = np.std(ga_elite_attempt_10_50, axis=0)
rw_elite_attempt_std_10_50 = np.std(rw_elite_attempt_10_50, axis=0)
ga_elite_attempt_std_20_50 = np.std(ga_elite_attempt_20_50, axis=0)
rw_elite_attempt_std_20_50 = np.std(rw_elite_attempt_20_50, axis=0)
ga_elite_attempt_std_30_50 = np.std(ga_elite_attempt_30_50, axis=0)
rw_elite_attempt_std_30_50 = np.std(rw_elite_attempt_30_50, axis=0)

ga_elite_attempt_std_10_100 = np.std(ga_elite_attempt_10_100, axis=0)
rw_elite_attempt_std_10_100 = np.std(rw_elite_attempt_10_100, axis=0)
ga_elite_attempt_std_20_100 = np.std(ga_elite_attempt_20_100, axis=0)
rw_elite_attempt_std_20_100 = np.std(rw_elite_attempt_20_100, axis=0)
ga_elite_attempt_std_30_100 = np.std(ga_elite_attempt_30_100, axis=0)
rw_elite_attempt_std_30_100 = np.std(rw_elite_attempt_30_100, axis=0)

ga_elite_mean_std_10_50 = sum(ga_elite_attempt_std_10_50)/m1
rw_elite_mean_std_10_50 = sum(rw_elite_attempt_std_10_50)/m1
ga_elite_mean_std_20_50 = sum(ga_elite_attempt_std_20_50)/m2
rw_elite_mean_std_20_50 = sum(rw_elite_attempt_std_20_50)/m2
ga_elite_mean_std_30_50 = sum(ga_elite_attempt_std_30_50)/m3
rw_elite_mean_std_30_50 = sum(rw_elite_attempt_std_30_50)/m3

ga_elite_mean_std_10_100 = sum(ga_elite_attempt_std_10_100)/m1
rw_elite_mean_std_10_100 = sum(rw_elite_attempt_std_10_100)/m1
ga_elite_mean_std_20_100 = sum(ga_elite_attempt_std_20_100)/m2
rw_elite_mean_std_20_100 = sum(rw_elite_attempt_std_20_100)/m2
ga_elite_mean_std_30_100 = sum(ga_elite_attempt_std_30_100)/m3
rw_elite_mean_std_30_100 = sum(rw_elite_attempt_std_30_100)/m3


N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
fig, ax = plt.subplots()
ga_ms_50 = (ga_elite_mean_std_10_50, ga_elite_mean_std_20_50, ga_elite_mean_std_30_50)
rw_ms_50 = (rw_elite_mean_std_10_50, rw_elite_mean_std_20_50, rw_elite_mean_std_30_50)
rects1 = ax.bar(ind, ga_ms_50, width, color='r')
rects2 = ax.bar(ind + width, rw_ms_50, width, color='y')
ax.set_ylabel('Média do Desvio Padrão')
ax.set_title('Média do Desvio Padrão pelo Tamanho da Palavra (Precisão) (População 50)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10','20','30'))
ax.legend((rects1[0], rects2[0]), ('AG', 'Random Walk'))
plt.show()

fig, ax = plt.subplots()
ga_ms_100 = (ga_elite_mean_std_10_100, ga_elite_mean_std_20_100, ga_elite_mean_std_30_100)
rw_ms_100 = (rw_elite_mean_std_10_100, rw_elite_mean_std_20_100, rw_elite_mean_std_30_100)
rects1 = ax.bar(ind, ga_ms_100, width, color='r')
rects2 = ax.bar(ind + width, rw_ms_50, width, color='y')
ax.set_ylabel('Média do Desvio Padrão')
ax.set_title('Média do Desvio Padrão pelo Tamanho da Palavra (Precisão) (População 100)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10','20','30'))
ax.legend((rects1[0], rects2[0]), ('AG', 'Random Walk'))
plt.show()

# Parte 3

t_norm_10 = np.array(target_normalized_data_10)
t_norm_20 = np.array(target_normalized_data_20)
t_norm_30 = np.array(target_normalized_data_30)

ga_hits_10_50_total = []
for i in range(5):
        ga_hits_10_50 = np.sum(t_norm_10 == ga_elite_attempt_10_50[i])
#        print(ga_hits_10_50)
        ga_hits_10_50_total.append(ga_hits_10_50)
ga_hits_mean_10_50 = np.mean(ga_hits_10_50_total)
ga_hits_std_10_50 = np.std(ga_hits_10_50_total)


ga_hits_20_50_total = []
for i in range(5):
        ga_hits_20_50 = np.sum(t_norm_20 == ga_elite_attempt_20_50[i])
#        print(ga_hits_10_50)
        ga_hits_20_50_total.append(ga_hits_20_50)
ga_hits_mean_20_50 = np.mean(ga_hits_20_50_total)
ga_hits_std_20_50 = np.std(ga_hits_20_50_total)

ga_hits_30_50_total = []
for i in range(5):
        ga_hits_30_50 = np.sum(t_norm_30 == ga_elite_attempt_30_50[i])
#        print(ga_hits_30_50)
        ga_hits_30_50_total.append(ga_hits_30_50)
ga_hits_mean_30_50 = np.mean(ga_hits_30_50_total)
ga_hits_std_30_50 = np.std(ga_hits_30_50_total)

ga_hits_10_100_total = []
for i in range(5):
        ga_hits_10_100 = np.sum(t_norm_10 == ga_elite_attempt_10_100[i])
#        print(ga_hits_10_100)
        ga_hits_10_100_total.append(ga_hits_10_100)
ga_hits_mean_10_100 = np.mean(ga_hits_10_100_total)
ga_hits_std_10_100 = np.std(ga_hits_10_100_total)


ga_hits_20_100_total = []
for i in range(5):
        ga_hits_20_100 = np.sum(t_norm_20 == ga_elite_attempt_20_100[i])
#        print(ga_hits_10_100)
        ga_hits_20_100_total.append(ga_hits_20_100)
ga_hits_mean_20_100 = np.mean(ga_hits_20_100_total)
ga_hits_std_20_100 = np.std(ga_hits_20_100_total)

ga_hits_30_100_total = []
for i in range(5):
        ga_hits_30_100 = np.sum(t_norm_30 == ga_elite_attempt_30_100[i])
#        print(ga_hits_30_50)
        ga_hits_30_100_total.append(ga_hits_30_100)
ga_hits_mean_30_100 = np.mean(ga_hits_30_100_total)
ga_hits_std_30_100 = np.std(ga_hits_30_100_total)


# RW

rw_hits_10_50_total = []
for i in range(5):
        rw_hits_10_50 = np.sum(t_norm_10 == rw_elite_attempt_10_50[i])
#        print(ga_hits_10_50)
        rw_hits_10_50_total.append(rw_hits_10_50)
rw_hits_mean_10_50 = np.mean(rw_hits_10_50_total)
rw_hits_std_10_50 = np.std(rw_hits_10_50_total)


rw_hits_20_50_total = []
for i in range(5):
        rw_hits_20_50 = np.sum(t_norm_20 == rw_elite_attempt_20_50[i])
#        print(ga_hits_10_50)
        rw_hits_20_50_total.append(rw_hits_20_50)
rw_hits_mean_20_50 = np.mean(rw_hits_20_50_total)
rw_hits_std_20_50 = np.std(rw_hits_20_50_total)

rw_hits_30_50_total = []
for i in range(5):
        rw_hits_30_50 = np.sum(t_norm_30 == rw_elite_attempt_30_50[i])
#        print(ga_hits_30_50)
        rw_hits_30_50_total.append(rw_hits_30_50)
rw_hits_mean_30_50 = np.mean(rw_hits_30_50_total)
rw_hits_std_30_50 = np.std(rw_hits_30_50_total)

rw_hits_10_100_total = []
for i in range(5):
        rw_hits_10_100 = np.sum(t_norm_10 == rw_elite_attempt_10_100[i])
#        print(ga_hits_10_100)
        rw_hits_10_100_total.append(rw_hits_10_100)
rw_hits_mean_10_100 = np.mean(rw_hits_10_100_total)
rw_hits_std_10_100 = np.std(rw_hits_10_100_total)


rw_hits_20_100_total = []
for i in range(5):
        rw_hits_20_100 = np.sum(t_norm_20 == rw_elite_attempt_20_100[i])
#        print(ga_hits_10_100)
        rw_hits_20_100_total.append(rw_hits_20_100)
rw_hits_mean_20_100 = np.mean(rw_hits_20_100_total)
rw_hits_std_20_100 = np.std(rw_hits_20_100_total)

rw_hits_30_100_total = []
for i in range(5):
        rw_hits_30_100 = np.sum(t_norm_30 == rw_elite_attempt_30_100[i])
#        print(ga_hits_30_50)
        rw_hits_30_100_total.append(rw_hits_30_100)
rw_hits_mean_30_100 = np.mean(rw_hits_30_100_total)
rw_hits_std_30_100 = np.std(rw_hits_30_100_total)


ga_hits_vector_mean_50 = [ga_hits_mean_10_50, ga_hits_mean_20_50, ga_hits_mean_30_50]
ga_hits_vector_std_50 = [ga_hits_std_10_50, ga_hits_std_20_50, ga_hits_std_30_50]

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, ga_hits_vector_mean_50, width, color='r', yerr=ga_hits_vector_std_50)

rw_hits_vector_mean_50 = [rw_hits_mean_10_50, rw_hits_mean_20_50, rw_hits_mean_30_50]
rw_hits_vector_std_50 = [rw_hits_std_10_50, rw_hits_std_20_50, rw_hits_std_30_50]

rects2 = ax.bar(ind + width, rw_hits_vector_mean_50, width, color='y', yerr=rw_hits_vector_std_50)

ax.set_ylabel('Total de Acertos')
ax.set_title('Média e Desvio Padrão do Total de Acertos (População 50)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10','20','30'))
ax.legend((rects1[0], rects2[0]), ('AG', 'Random Walk'))
plt.show()

ga_hits_vector_mean_100 = [ga_hits_mean_10_100, ga_hits_mean_20_100, ga_hits_mean_30_100]
ga_hits_vector_std_100 = [ga_hits_std_10_100, ga_hits_std_20_100, ga_hits_std_30_100]

fig, ax = plt.subplots()
rects1 = ax.bar(ind, ga_hits_vector_mean_100, width, color='r', yerr=ga_hits_vector_std_100)


rw_hits_vector_mean_100 = [rw_hits_mean_10_100, rw_hits_mean_20_100, rw_hits_mean_30_100]
rw_hits_vector_std_100 = [rw_hits_std_10_100, rw_hits_std_20_100, rw_hits_std_30_100]

rects2 = ax.bar(ind + width, rw_hits_vector_mean_100, width, color='y', yerr=rw_hits_vector_std_100)

ax.set_ylabel('Total de Acertos')
ax.set_title('Média e Desvio Padrão do Total de Acertos (População 100)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10','20','30'))
ax.legend((rects1[0], rects2[0]), ('AG', 'Random Walk'))
plt.show()

# Parte 4
ga_elite_fit_attempt_bests_10_50 = ga_elite_fit_attempt_10_50[:,n1-1]
ga_elite_fit_attempt_bests_mean_10_50 = np.mean(ga_elite_fit_attempt_bests_10_50)
ga_elite_fit_attempt_bests_std_10_50 = np.std(ga_elite_fit_attempt_bests_10_50)

ga_elite_fit_attempt_bests_20_50 = ga_elite_fit_attempt_20_50[:,n2-1]
ga_elite_fit_attempt_bests_mean_20_50 = np.mean(ga_elite_fit_attempt_bests_20_50)
ga_elite_fit_attempt_bests_std_20_50 = np.std(ga_elite_fit_attempt_bests_20_50)

ga_elite_fit_attempt_bests_30_50 = ga_elite_fit_attempt_30_50[:,n3-1]
ga_elite_fit_attempt_bests_mean_30_50 = np.mean(ga_elite_fit_attempt_bests_30_50)
ga_elite_fit_attempt_bests_std_30_50 = np.std(ga_elite_fit_attempt_bests_30_50)

ga_elite_fit_attempt_bests_10_100 = ga_elite_fit_attempt_10_100[:,n1-1]
ga_elite_fit_attempt_bests_mean_10_100 = np.mean(ga_elite_fit_attempt_bests_10_100)
ga_elite_fit_attempt_bests_std_10_100 = np.std(ga_elite_fit_attempt_bests_10_100)

ga_elite_fit_attempt_bests_20_100 = ga_elite_fit_attempt_20_100[:,n2-1]
ga_elite_fit_attempt_bests_mean_20_100 = np.mean(ga_elite_fit_attempt_bests_20_100)
ga_elite_fit_attempt_bests_std_20_100 = np.std(ga_elite_fit_attempt_bests_20_100)

ga_elite_fit_attempt_bests_30_100 = ga_elite_fit_attempt_30_100[:,n3-1]
ga_elite_fit_attempt_bests_mean_30_100 = np.mean(ga_elite_fit_attempt_bests_30_100)
ga_elite_fit_attempt_bests_std_30_100 = np.std(ga_elite_fit_attempt_bests_30_100)

# rw
rw_elite_fit_attempt_bests_10_50 = rw_elite_fit_attempt_10_50[:,n1-1]
rw_elite_fit_attempt_bests_mean_10_50 = np.mean(rw_elite_fit_attempt_bests_10_50)
rw_elite_fit_attempt_bests_std_10_50 = np.std(rw_elite_fit_attempt_bests_10_50)

rw_elite_fit_attempt_bests_20_50 = rw_elite_fit_attempt_20_50[:,n2-1]
rw_elite_fit_attempt_bests_mean_20_50 = np.mean(rw_elite_fit_attempt_bests_20_50)
rw_elite_fit_attempt_bests_std_20_50 = np.std(rw_elite_fit_attempt_bests_20_50)

rw_elite_fit_attempt_bests_30_50 = rw_elite_fit_attempt_30_50[:,n3-1]
rw_elite_fit_attempt_bests_mean_30_50 = np.mean(rw_elite_fit_attempt_bests_30_50)
rw_elite_fit_attempt_bests_std_30_50 = np.std(rw_elite_fit_attempt_bests_30_50)

rw_elite_fit_attempt_bests_10_100 = rw_elite_fit_attempt_10_100[:,n1-1]
rw_elite_fit_attempt_bests_mean_10_100 = np.mean(rw_elite_fit_attempt_bests_10_100)
rw_elite_fit_attempt_bests_std_10_100 = np.std(rw_elite_fit_attempt_bests_10_100)

rw_elite_fit_attempt_bests_20_100 = rw_elite_fit_attempt_20_100[:,n2-1]
rw_elite_fit_attempt_bests_mean_20_100 = np.mean(rw_elite_fit_attempt_bests_20_100)
rw_elite_fit_attempt_bests_std_20_100 = np.std(rw_elite_fit_attempt_bests_20_100)

rw_elite_fit_attempt_bests_30_100 = rw_elite_fit_attempt_30_100[:,n3-1]
rw_elite_fit_attempt_bests_mean_30_100 = np.mean(rw_elite_fit_attempt_bests_30_100)
rw_elite_fit_attempt_bests_std_30_100 = np.std(rw_elite_fit_attempt_bests_30_100)

ga_elite_fit_attempt_bests_vector_mean_50 = [ga_elite_fit_attempt_bests_mean_10_50, ga_elite_fit_attempt_bests_mean_20_50, ga_elite_fit_attempt_bests_mean_30_50]
ga_elite_fit_attempt_bests_vector_std_50 = [ga_elite_fit_attempt_bests_std_10_50, ga_elite_fit_attempt_bests_std_20_50, ga_elite_fit_attempt_bests_std_30_50]

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, ga_elite_fit_attempt_bests_vector_mean_50, width, color='r', yerr=ga_elite_fit_attempt_bests_vector_std_50)

rw_elite_fit_attempt_bests_vector_mean_50 = [rw_elite_fit_attempt_bests_mean_10_50, rw_elite_fit_attempt_bests_mean_20_50, rw_elite_fit_attempt_bests_mean_30_50]
rw_elite_fit_attempt_bests_vector_std_50 = [rw_elite_fit_attempt_bests_std_10_50, rw_elite_fit_attempt_bests_std_20_50, rw_elite_fit_attempt_bests_std_30_50]

rects2 = ax.bar(ind + width, rw_elite_fit_attempt_bests_vector_mean_50, width, color='y', yerr=rw_elite_fit_attempt_bests_vector_std_50)

ax.set_ylabel('Desvio')
ax.set_title('Média e Desvio Padrão do Desvio da Palavra encontrada da alvo (Acurácia) (População 50)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10','20','30'))
ax.legend((rects1[0], rects2[0]), ('AG', 'Random Walk'))
plt.show()

ga_elite_fit_attempt_bests_vector_mean_100 = [ga_elite_fit_attempt_bests_mean_10_100, ga_elite_fit_attempt_bests_mean_20_100, ga_elite_fit_attempt_bests_mean_30_100]
ga_elite_fit_attempt_bests_vector_std_100 = [ga_elite_fit_attempt_bests_std_10_100, ga_elite_fit_attempt_bests_std_20_100, ga_elite_fit_attempt_bests_std_30_100]

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, ga_elite_fit_attempt_bests_vector_mean_100, width, color='r', yerr=ga_elite_fit_attempt_bests_vector_std_100)

rw_elite_fit_attempt_bests_vector_mean_100 = [rw_elite_fit_attempt_bests_mean_10_100, rw_elite_fit_attempt_bests_mean_20_100, rw_elite_fit_attempt_bests_mean_30_100]
rw_elite_fit_attempt_bests_vector_std_100 = [rw_elite_fit_attempt_bests_std_10_100, rw_elite_fit_attempt_bests_std_20_100, rw_elite_fit_attempt_bests_std_30_100]

rects2 = ax.bar(ind + width, rw_elite_fit_attempt_bests_vector_mean_100, width, color='y', yerr=rw_elite_fit_attempt_bests_vector_std_100)

ax.set_ylabel('Desvio')
ax.set_title('Média e Desvio Padrão do Desvio da Palavra encontrada da alvo (Acurácia) (População 100)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('10','20','30'))
ax.legend((rects1[0], rects2[0]), ('AG', 'Random Walk'))
plt.show()