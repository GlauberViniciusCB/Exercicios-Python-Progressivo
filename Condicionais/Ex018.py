#  Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar 
#  quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo 
#  é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
# nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 
# 10, uma nota de 5 e quatro notas de 1.
print('\033[33m=\033[m' *155)
print('                                                           Bem Vindo Ao Caixa ')
print('\033[33m=\033[m' *155)
print('\033[31;41mATENÇÃO: O VALOR MÍNIMO É DE R$10 E O MÁXIMO É DE R$600.\033[m')
quant = float(input('\033[mInforme A Quantidade Deseja Tirar No Caixa: R$'))
total = quant
if(quant >=10 and quant<=600):
    if(quant >= 100 ):
        final = quant//100
        notas = final *100
        total = total - notas
        quant = total
        print('\033[32mO Retorno Será De \033[m{:.0f}\033[32m Notas De: \033[mR$100 '.format(final))
    if(quant<= 50 or quant > 0 ):
         final = quant//50
         notas = final *50
         total = total - notas
         quant = total 
         print('\033[32mO Retorno Será De \033[m{:.0f}\033[32m Notas De: \033[mR$50 '.format(final))  
    if(quant <= 10 or quant > 0):
        final = quant //10
        nota = final * 10
        total = total - nota 
        quant = total 
        print('\033[32mO Retorno Será De \033[m{:.0f}\033[32m Notas De: \033[mR$10 '.format(final))
    if(quant <=5 or quant > 0):
        final = quant //5
        nota = final * 5
        total = total - nota 
        quant = total 
        print('\033[32mO Retorno Será De \033[m{:.0f}\033[32m Notas De: \033[mR$5 '.format(final))
    if(quant <= 1 or quant > 0):
        final = quant //1
        nota = final * 1
        total = total - nota 
        quant = total 
        print('\033[32mO Retorno Será De \033[m{:.0f}\033[32m Notas De: \033[mR$1' .format(final))
else:
    print('\033[31;41mNão É Permitido Sacar Este Valor!\033[m')
