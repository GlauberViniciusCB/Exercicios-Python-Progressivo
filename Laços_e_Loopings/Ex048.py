# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
# 12376489
# => 98467321
num = []
num = int(input('Digite Um Número Inteiro Positivo: ')) 
print(f'O Número Digitado: {num}')
num = str(num)
print(f'O Número Invertido: {num[::-1]}')