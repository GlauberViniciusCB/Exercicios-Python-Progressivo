# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# Altere:o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Informe O 1° Termo: '))
num2 = int(input('Informe O 2° Termo: '))
cont = num1 + 1
soma = 0

while(cont < num2):
    print(cont,end =' ')
    soma = soma + cont
    cont = cont + 1
print(f'\nSoma Dos Termos Entre {num1} E {num2} É: {soma}')
