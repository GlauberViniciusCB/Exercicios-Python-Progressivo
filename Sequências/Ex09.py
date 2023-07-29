# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do 
# vetor.
vet = []
for i in range(10):
    num = int(input('Digite Um Número: '))
    quad= num**2
    vet.append(quad)
print(sum(vet))