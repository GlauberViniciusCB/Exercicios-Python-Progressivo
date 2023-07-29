# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
num1 = int(input('Informe O 1° Número Inteiro: '))
num2 = int(input('Informe O 2° Número Inteiro: '))
num3 = int(input('Informe O 3° Número Inteiro: '))
menor = 0 
maior = 0

if(num1 > num2 and num1 > num3):
    maior = num1
elif(num2 > num1 and num2 > num3):
    maior = num2
elif(num3 > num1 and num3 > num2):
    maior = num3 


if(num1 < num2 and num1 < num3):
    menor = num1 
elif(num2 < num1 and num2 < num3 ):
    menor = num2
elif (num3 < num1 and num3 < num2):
    menor = num3 


print('O Maior Número Entre Os Digitados É {} E O Menor É {} '.format(maior,menor) )

