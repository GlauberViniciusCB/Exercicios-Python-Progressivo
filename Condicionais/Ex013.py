# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa deverá pedir os 
# valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# e o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir 
# os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# PS: digite 'import math' no início de seu script. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)
from math import sqrt

a = float (input('\nInforme O Valor De "A": '))
b = float (input('Informe O Valor De "B": '))
c = float (input('Informe O Valor De "C": '))

formula= b**2-4*(a*c)
if(a == 0):
    print('A Equação Não É Do Segundo Grau!')
else:
    formula= b**2-4*(a*c)
    total = formula
    delta = sqrt(total)
    print('{:.0f}'.format(delta))
    if(delta < 0 ):
        print('A Equação Não Possui Raizes Reais.')
    elif(delta == 0 ): 
         x1 = (-b + delta )/2*a
         x2 = (-b - delta )/2*a
         print('A Equação  Possui Apenas Uma Raiz Real.')
         print('E São Ela: {} E {} .'.format(x1,x2))
    else:
        x1 = (-b + delta )/2*a
        x2 = (-b - delta )/2*a
        print('A Equação  Possui Duas Raizes Reais.')
        print('E São Elas: {} E {} .'.format(x1,x2))