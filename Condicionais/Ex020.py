# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1  = float(input('\nInforme O 1° Número: '))
num2  = float(input('Informe O 2° Número: '))
opcao = int(input('\nEscolha Uma Opção:\n[1] - Adição \n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n'))

if(opcao >= 1 and opcao <= 4):
    if(opcao == 1):
        print('Sua Escolha Foi Soma:')
        res = num1 + num2
        print('Resultado: {}'.format(res))
    elif(opcao == 2):
        print('Sua Escolha Foi Subtração:')
        res = num1 - num2
        print('Resultado: {}'.format(res))
    elif(opcao == 3):
        print('Sua Escolha Foi Multiplicação:')
        res = num1 * num2
        print('Resultado: {}'.format(res))
    elif(opcao == 4):
        print('Sua Escolha Foi Divição:')
        res= num1 / num2
        print('Resultado: {}'.format(res)) 
else:
    print('\n033[31mOpção Invalida!\033[m')

if(res %2 ==0):
    print('É Par!')
else:
    print('É Impar!')

if(res > 0):
    print('O Número É Positivo!')
elif(res < 0 ):
    print('O Número É Negativo!')
else:
    print('O Número É Neutro!')

aux =round(res) 
if(res == aux):
    print('É Um Número Inteiro!')
else:
    print('É Um Número Decimal!')


