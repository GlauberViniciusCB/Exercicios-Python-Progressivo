# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
# mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades.
num = int (input('\nInforme Um Número Menor 1000: '))
if(num > 1000):
    print('Número Inválido!')
else:
    print('\n\033[33mO Número Digitado foi : {} É Composto Por: \033[m'.format(num))
    centena = (num//100) % 10
    if(centena <= 1):
        print('{} Centena,'.format (centena),end = ' ')
    else:
        print('{} Centenas,'.format (centena),end = ' ')
    
    dezena  = (num//10) % 10
    if(dezena <= 1):
         print('{} Dezena,'.format (dezena),end = ' ')
    else:
         print('{} Dezenas,'.format (dezena),end = ' ')
    
    unidade = (num//1) % 10
    if( unidade<= 1):
        print('{} E Unidade.'.format(unidade),end=' ')
    else:
        print('{} E Unidades.'.format(unidade),end=' ')
