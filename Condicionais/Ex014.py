# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não 
# bissexto.

ano = int (input('Informe Um Ano : '))
if( ano %100 != 0 and ano % 4 == 0 or ano % 400 == 0 ):
    print('O Ano {} É Bissexto!'.format(ano))
else:
   print('O Ano {} Não É Bissexto!'.format(ano))
