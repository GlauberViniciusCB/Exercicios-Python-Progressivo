# Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número através
# de outra função.

def Maior ():
    maior = numeros[0]
    for num in (numeros):
        if(num > maior):
            maior = num
    print(f'O Maior Número É {maior}.')

def Menor():
    menor = numeros[0]
    for num in numeros:
        if(num < menor):
            menor = num
    print(f'O Menor Número ´É {menor}.') 
numeros = []
i = 1
while(i <= 3):
    num = int(input('Digite Um Número: '))
    numeros.append(num) 
    i = i + 1
print(f'\n Os Números Digitados Foram: {numeros}')
Maior()
Menor()
