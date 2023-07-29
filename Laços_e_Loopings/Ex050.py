# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
soma = 0
num = int(input('Digite Um Número: '))
h = 1
print('1',end =' + ')
cont = 2
while(cont <= num):
    if(cont < num):
        print(f'{h}/{cont} + ', end= '')
    elif(cont == num):
        print(f'{h}/{cont}',end ='')
    soma = soma + cont   
    cont = cont + 1
print(f'\nResultado Final De H = {num}/{soma}')