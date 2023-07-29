# Faça um programa que leia 5 números e informe a soma e a média dos números
i = 1
soma = 0
media = 0 
while(i <= 5):
    num = int(input(f'Informe O {i}° Número: '))
    soma = soma + num  
    i = i + 1
    media = soma/5
print('\n')
print(f'A Soma De Todos Os Números Digitados Foi {soma}')
print(f'A Média É: {media}')