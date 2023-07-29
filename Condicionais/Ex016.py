# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo 
# (resto da divisão): %
num = int (input('Informe Um Número Inteiro: '))
if(num% 2 == 0):
    print('\033[33mO Número {} É Par.\033[m'.format(num))
else: 
    print('\033[33mO Número {} É Impar.\033[m'.format(num))
