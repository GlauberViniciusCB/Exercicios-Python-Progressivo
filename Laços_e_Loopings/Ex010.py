# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int (input('Informe O 1° Número: '))
num2 = int (input('Informe O 2° Número: '))
cont = num1 + 1

while(cont < num2):
    print(cont,end =' ')
    cont = cont+1
