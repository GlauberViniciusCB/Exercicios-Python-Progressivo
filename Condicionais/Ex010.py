# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar 
# outro valor deve aparecer valor inválido.
num = int(input('Informe Um Número Entre 1 E 7: '))
if(num == 1):
    print('Hoje É Domingo!')
elif(num == 2):
    print('Hoje É Segunda!')
elif(num == 3):
    print('Hoje É Terça!')
elif(num == 4):
    print('Hoje É Quarta!')
elif(num == 5):
    print('Hoje É Quinta!')
elif(num == 6):
    print('Hoje É Sexta!')
elif(num == 7):
    print('Hoje É Sabado!')
elif(num < 1 or num > 7):
    print('Valor Invalido!')
