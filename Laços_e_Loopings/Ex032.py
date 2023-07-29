# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve 
# ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120
i = 1
fat = 1
num = int(input('Informe O Número Inteiro: '))
i = num 
print(f'{i}! =',end=' ')
while(i >= 1):
    fat = i * fat
    if(i == 1):
        print(i,end= ' ')
    else:
        print(i,end =' . ')
    i = i - 1
print(f'= {fat}')