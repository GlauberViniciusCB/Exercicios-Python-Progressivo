# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.
soma = 0
num = int(input('Informe Um Número: '))
cont = 1
soma_total_num = 0
soma_total_soma = 0
while (cont < num):
    if(cont == 1):
        print(f'{cont}/{soma+1}')
        soma = soma + 1
    else: 
        print(f'{cont}/{soma}')
    cont = cont + 1  
    soma = soma + 2
# print(soma)
# print(cont)