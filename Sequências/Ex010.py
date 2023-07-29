# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores 
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vet_1 = []
vet_2 = []
vet_3 = []
for i in range (10):
    vet_1.append(int(input('Digite Um Número Para O 1° Vetor: ')))
for j in range (10):
    vet_2.append(int(input('Digite Um Número Para O 2° Vetor: ')))

print(f'O 1° Vetor: {vet_1}')
print(f'O 2° Vetor: {vet_2}')
for k in range (1):
    vet_3.append(vet_1 + vet_2)
print(f'A Junção Dos Dois É: {vet_3}')