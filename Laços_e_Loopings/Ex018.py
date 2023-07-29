# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
cont = 1
maior = 0
menor = 0
soma = 0
n = int (input(f'Informe Quantos Números Você Deseja Digitar: ')) 
for cont in range (n):
   n = int (input(f'Digite o {cont+1}° Número: ')) 
   soma = soma + n   
   cont = cont + 1
   if(cont == 1):
    maior = n
    menor = n
   else:
        if(n > maior):
            maior = n
        if(n < menor):
            menor = n
print('\n')
print(f'O Maior Número Entre Os Digitados É: {maior}')
print(f'O Menor Número Entre Os Digitados É: {menor}')
print(f'A Soma De Todos Os Números Digitados É: {soma}')
