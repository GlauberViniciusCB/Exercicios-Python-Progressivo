# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é 
# divisível somente por ele mesmo e por 1.
i = 1
primo = 0
num = int(input('Informe Um Número Inteiro: '))
while(i <= 9 ):
    quant_div =  num%i
    if(quant_div == 0):
        primo = primo+1
    i = i + 1
if(primo <= 2):
    print(f'\033[32mO Número {num} É Primo!\033[m')
else:
    print(f'\033[31mO Número {num} Não É Primo!\033[m')

