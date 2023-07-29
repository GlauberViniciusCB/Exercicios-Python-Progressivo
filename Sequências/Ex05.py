# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
# números IMPARES no vetor impar. Imprima os três vetores.
vet = []
vet_par = []
vet_imp = []
for i in range (20):
    num = (int(input('Digite Um Número: ')))
    vet.append(num)
    if(num % 2 == 0):
        vet_par.append(num)
    else:
        vet_imp.append(num)
print(f'Todos Os Números : {vet}')
print(f'Números Pares: {vet_par}')
print(f'Números Impares: {vet_imp}')
