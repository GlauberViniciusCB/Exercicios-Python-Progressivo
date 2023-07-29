# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
lista_0_25 = []
lista_26_50 = []
lista_51_75 = []
lista_76_100 = []
while True:
    num = int(input('Informe Um Número Positivo, Caso Queira Encerrar Digite Um Número Negativo: '))
    while(num > 100):
        print('Número Inválido, Tente Um Número Entre 0 E 100. ')
        num = int(input('Informe Um Número Positivo, Caso Queira Encerrar Digite Um Número Negativo: '))
    if(num >= 0 and num <= 25):
        lista_0_25.append(num)
    if(num >= 26 and num <= 50):
        lista_26_50.append(num)
    if(num >= 51 and num <= 75):
        lista_51_75.append(num)
    if(num >= 76 and num <= 100):
        lista_76_100.append(num)
    if(num < 0):
        print('Programa Finalizado.')
        break
print(f'A Quantidade De Número Digitados Entre [0 - 25] : {len(lista_0_25)}')
print(f'A Quantidade De Número Digitados Entre [26 - 50]: {len(lista_26_50)}')
print(f'A Quantidade De Número Digitados Entre [51 - 75]: {len(lista_51_75)}')
print(f'A Quantidade De Número Digitados Entre [76 - 100: {len(lista_76_100)}')