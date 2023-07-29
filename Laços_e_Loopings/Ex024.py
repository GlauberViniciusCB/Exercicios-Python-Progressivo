# Faça um programa que calcule e mostre a média aritmética de N notas.
cont = 0
soma = 0
while True:
    n = float(input(f'Digite A \033[31m{cont+1}°\033[m Nota Ou \033[33m0\033[m Para Encerrar: '))
    soma = soma + n 
    if(n == 0):
        break
    cont = cont + 1 
media =soma/cont
print(f'A Média Das Notas Digitadas É: {media:.2f} ')
