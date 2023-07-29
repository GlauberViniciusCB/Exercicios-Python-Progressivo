# Faça um Programa que leia três números e mostre-os em ordem decrescente.
# Algoritmo:
# 1. Compara as duas últimas posições
# 2. Compara as duas primeiras posições
# 3. Compara novamente as duas últimas posições

num1 = int (input('Informe O 1° Número:'))
num2 = int (input('Informe O 2° Número: '))
num3 = int (input('Informe O 3° Número: '))

if (num3  > num2):
    aux  = num3
    num3 = num2
    num2 = aux

if (num2 > num1):
    aux  = num2
    num2 = num1
    num1 = aux

if (num3 > num2) :
    aux = num3
    num3 = num2
    num2 = aux


print(num1,num2,num3)

