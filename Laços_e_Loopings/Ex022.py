# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é 
# divisível somente por ele mesmo e por 1
# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é 
# divisível.
j = 1
primo = 0
div = []
num = int (input('Informe Um Número Inteiro: ')) 
while(j <= 9):
    total = num % j 
    if(total == 0):
        primo = primo + 1
        div.append(j)
    j= j + 1  
print('\n')  
if(primo == 2):
    print(f'\033[32mO Número {num} É Primo!\033[m')
else:
    print(f'\033[31mO Número {num} Não É Primo! \033[m')
    print(f'\033[33mO Número {num} É Divisível Por {div}\033[m')