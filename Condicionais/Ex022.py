# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool: 
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago 
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
from time import sleep
print('=*=*'*39)
print('\033[33m                                                           Olá, Como Deseja Abastecer? \033[m')
print('=*=*'*39)
print('\033[31mDigite:\033[m\nA - Álcool\nG - Gasolina')
escolha = str(input()).upper()
if(escolha == 'A' or escolha == 'G'):
    quant   = float(input('\n\033[33mQuantos Litros Você Deseja Abastecer? \033[m')) 
    if(escolha == 'A' and quant <= 20):
        pt = 1.90 * quant
        des = pt * 0.03
        final = pt - des
        print('\033[34mCalculando...\033[m')
        sleep(3)
        print('Valor Integral: R${:.2f}'.format(pt))
        print('\033[32mVocê Recebeu 3% De Desconto.\033[m')
        print('Por {} Litro(s) De Álcool, O Valor A Ser Pago Será De R$ {:.2f}'.format(quant,final))
    elif(escolha == 'A' and quant > 20):
        pt = 1.90 * quant
        des = pt * 0.05
        final = pt - des 
        print('\033[34mCalculando...\033[m')
        sleep(3)
        print('Valor Integral: R${:.2f}'.format(pt))
        print('\033[32mVocê Recebeu 5% De Desconto.\033[m')
        print('Por {} Litro(s) De Álcoool, O Valor A Ser Pago Será De R$ {:.2f}'.format(quant,final))
    if(escolha == 'G' and quant <= 20):
        pt = 2.50 * quant
        des = pt * 0.04
        final = pt - des 
        print('\033[34mCalculando...\033[m')
        sleep(3)
        print('Valor Integral: R${:.2f}'.format(pt))
        print('\033[32mVocê Recebeu 4% De Desconto.\033[m')
        print('Por {} Litro(s) De Gasolina, O Valor A Ser Pago Será De R$ {:.2f}'.format(quant,final))
    elif(escolha == 'G' and quant > 20):
        pt = 2.50 * quant
        des = pt * 0.06
        final = pt - des 
        print('\033[34mCalculando...\033[m')
        sleep(3)
        print('Valor Integral: R${:.2f}'.format(pt))
        print('\033[32mVocê Recebeu 6% De Desconto.\033[m')
        print('Por {} Litro(s) De Gasolina, O Valor A Ser Pago Será De R$ {:.2f}'.format(quant,final))
else:
    print('\n\033[31mOpção Inválida!\033[m')
