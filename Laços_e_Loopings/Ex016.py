# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
# valor seja maior que 500.
cont = 0
num = 500
termo1 = 0
termo2 = 1
while(cont < num):
    soma = termo1 + termo2
    print(soma, end= ' ')
    termo1 = termo2
    termo2 = soma
    cont = cont + 1 
    if(soma > 500):
        break
