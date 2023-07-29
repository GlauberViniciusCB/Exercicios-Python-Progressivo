# Faça um Programa que leia três números inteiros e mostre o maior deles.
num1 = int(input('Informe O 1° Número Inteiro: '))
num2 = int(input('Informe O 2° Número Inteiro: '))
num3 = int(input('Informe O 3° Número Inteiro: ')) 

if (num1 > num2 and num1 > num3 ):
    print('O 1° Número É O Maior Entre Os Digitados.')
elif(num2 > num1 and num2 > num3 ):
    print('O 2° Número É O Maior Entre Os Digitados.')
elif(num3 > num1 and num3 > num2):
    print('O 3° Número É O Maior Entre Os Digitados.')
else: 
    print('Não Há Um Número Maior, Entre Os Digitados.')