# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores 
# deverão ser compostos pelos elementos intercalados dos dois outros vetores Altere o programa, intercalando 3 vetores 
# de 10 elementos cada.
vet_1 = [] 
vet_2 = []
vet_3 = []
for i in range (10):
    num = int(input('Digite Um Número Para O 1° Vetor: '))
    vet_1.append(num)
for i in range (10):
    num = int(input('Digite Um Número Para O 2° Vetor: '))
    vet_2.append(num)

for i in range(10):
    vet_3.append(vet_1[i])
    vet_3.append(vet_2[i])
print(vet_3)