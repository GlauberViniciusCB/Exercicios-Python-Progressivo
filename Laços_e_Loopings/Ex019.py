# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores aceite
# apenas números entre 0 e 1000.
i = 0
maior = 0
menor = 0
soma = 0
num = int(input('Informe A Quantidade De Números Que Deseja Digitar: '))
if(num < 0):
    print('\033[31mQuantidade Inválida!\033[m')
while (i < num):
    n = int(input(f'Informe O {i+1}° Número: '))
    if(n < 0 or n > 1000):
        print('\033[31mNúmero Inválido.\033[m')
        while(n < 0 and n > 1000):
            n = int(input(f'Informe O {i}° Número: '))
    else:
        i= i + 1
        soma = soma + n 
        if(i == 1):
            maior = n
            menor = n
        else:
            if(n > maior):
                maior = n
            if(n < menor):
                menor = n
print('\n')
print(f'\033[32mO Maior Termo\033[m: {maior}')
print(f'\033[32mO Menor Termo\033[m : {menor}')
print(f'\033[32mA Soma  Termo\033[m: {soma}')
          
