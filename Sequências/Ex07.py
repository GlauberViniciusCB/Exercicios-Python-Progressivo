# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vet = []
soma = 0 
resultado = 1
for numero in range (5):
    num = int(input(f'Informe O {numero+1}° Número: '))
    vet.append(num)
soma = sum(vet)
print('\n')
print(f'O Elementos Do Vetor São: {vet}')
print(f'A Soma De Todos Os Elementos Do Vetor É: {soma}')
for mult in vet:
    resultado = mult * resultado
print(f'A Multiplicação De Todos Os Elementos Do Vetor É: {resultado}')