# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vet = []
for i in range (10):
    vet.append(int(input('Informe Um Número: ')))
vet.reverse()
print(vet)