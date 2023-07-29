# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de 
# arredondamento.
num = float(input('Informe Um Número: '))
aux = round(num)

if(num == aux):
    print('O Número É Inteiro.')
else:
    print('O Número É Decimal.')