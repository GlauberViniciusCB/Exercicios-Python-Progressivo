# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = int(input('Informe O Número Que Deseja Ver O Resultado Do Fatorial:'))
resul = 1
cont = 1
while (cont <= num):
    resul = resul* cont
    cont = cont + 1
print(f'O Resultado Do Fatorial De {num} É: {resul}')