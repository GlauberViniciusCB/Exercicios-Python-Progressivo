# Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na 
# tela
num =  int(input('Informe O 1° Número Inteiro: ')) 
num2 = int(input('Informe O 2° Número Inteiro: '))

aux = num
num = num2
num2 = aux

print('Trocando Os Valores : O 1° Número Vale {} E O 2° Número Vale {}'.format(num,num2))