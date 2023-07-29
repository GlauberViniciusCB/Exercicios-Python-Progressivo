# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através
# de uma função. Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a
# primeira.
def Soma():
    n1 = int(input('Digite O 1° Número: '))
    n2 = int(input('Digite O 2° Número: '))
    n3 = int(input('Digte O 3° Número: '))
    soma = n1+n2+n3
    print(f'\nValores Digitados Foram [{n1}] [{n2}] [{n3}] ')
    return soma  
def Media ():
     media = (Soma())/3
     return print(f'A Média Dos Valores: {media:.2f}')


Media()