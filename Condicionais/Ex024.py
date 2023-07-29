# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                        Até 5 Kg               Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra           R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha          R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há 
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um 
# desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo 
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo 
# de pagamento, valor do desconto e valor a pagar.
from time import sleep
print('\033[33m=*=*\033[m'*35)
print('                                                              \033[31mHipermercado Tabajara\033[m')
print('\033[33m=*=*\033[m'*35)
print('''\033[32mO Hipermercado Tabajara está com uma promoção de carnes que é imperdível.\033[m \nConfira:
                    |          Até 5 Kg         |      Acima de 5 Kg
   ------------------------------------------------------------------
   [1]- File Duplo  |     R$ 4,90 por Kg        |    R$ 5,80 por Kg
   [2]- Alcatra     |     R$ 5,90 por Kg        |    R$ 6,80 por Kg
   [3]- Picanha     |     R$ 6,90 por Kg        |    R$ 7,80 por Kg''')

tipo = int(input('\nEscolha O Tipo De Carne Através Do Indice: '))

print('\n')
if(tipo >=1 and tipo<=3 ):
    if(tipo == 1):
        print('Sua Escolha Foi:\033[33m File Duplo.\033[m')
        quant = float(input('Quantos kg Deseja Comprar:'))
        if(quant > 0 and quant <= 5):
            preco = quant * 4.90
            print('\033[32mQual Será A Forma De Pagamento:\033[m \n[1] - Dinheiro.\n[2] - Cartão Tabajara.')
            forma = int(input())
            if(forma == 1):
                Tp = 'Dinheiro'
                des = 0 
                Tip = 'File Duplo'
            elif(forma == 2):
                Tp = 'Cartão Tabajara'
                des = preco*0.05
                final = preco - des
                Tip ='File Duplo'
            print('\033[34mAguarde Um Instante Estamos Emitindo O Cupom Fiscal...\033[m')
            sleep(2)
            print('\033[34m.......\033[m')
            sleep(4)
            print('\n\n\033[32m******* CUPOM FISCAL *******\033[m')
            if(forma == 1):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,preco))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
            elif(forma == 2):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,final))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
        elif(quant > 5):
            preco = quant * 5.80
            print('\033[32mQual Será A Forma De Pagamento:\033[m \n[1] - Dinheiro.\n[2] - Cartão Tabajara.')
            forma = int(input())
            if(forma == 1):
                Tp = 'Dinheiro'
                des = 0 
                Tip = 'File Duplo'
            elif(forma == 2):
                Tp = 'Cartão Tabajara'
                des = preco*0.05
                final = preco - des
                Tip ='File Duplo'
            print('\033[34mAguarde Um Instante Estamos Emitindo O Cupom Fiscal...\033[m')
            sleep(2)
            print('\033[34m.......\033[m')
            sleep(4)
            print('\n\n\033[32m******* CUPOM FISCAL *******\033[m')
            if(forma == 1):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,preco))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
            elif(forma == 2):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,final))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
        elif(quant <=0 ):
            print('\033[34mNão É Possivel Comprar:\033[m {}Kg'.format(quant))
    if(tipo == 2):
        print('Sua Escolha Foi:\033[33m Alcatra.\033[m')
        quant = float(input('Quantos kg Deseja Comprar:'))
        if(quant >0 and quant <=5 ):
            preco = quant * 5.90
            print('\033[32mQual Será A Forma De Pagamento:\033[m \n[1] - Dinheiro.\n[2] - Cartão Tabajara.')
            forma = int(input())
            if(forma == 1):
                Tp = 'Dinheiro'
                des = 0 
                Tip = 'Alcatra'
            elif(forma == 2):
                Tp = 'Cartão Tabajara'
                des = preco*0.05
                final = preco - des
                Tip ='Alcatra'
            print('\033[34mAguarde Um Instante Estamos Emitindo O Cupom Fiscal...\033[m')
            sleep(2)
            print('\033[34m.......\033[m')
            sleep(4)
            print('\n\n\033[32m******* CUPOM FISCAL *******\033[m')
            if(forma == 1):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,preco))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
            elif(forma == 2):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,final))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
        elif(quant > 5):
            preco = quant * 6.80
            print('\033[32mQual Será A Forma De Pagamento:\033[m \n[1] - Dinheiro.\n[2] - Cartão Tabajara.')
            forma = int(input())
            if(forma == 1):
                Tp = 'Dinheiro'
                des = 0 
                Tip = 'Alcatra'
            elif(forma == 2):
                Tp = 'Cartão Tabajara'
                des = preco*0.05
                final = preco - des
                Tip ='Alcatra'
            print('\033[34mAguarde Um Instante Estamos Emitindo O Cupom Fiscal...\033[m')
            sleep(2)
            print('\033[34m.......\033[m')
            sleep(4)
            print('\n\n\033[32m******* CUPOM FISCAL *******\033[m')
            if(forma == 1):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,preco))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
            elif(forma == 2):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,final))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
        elif(quant <=0 ):
            print('\033[34mNão É Possivel Comprar:\033[m {}Kg'.format(quant))
    if(tipo == 3):
        print('Sua Escolha Foi:\033[33m Picanha.\033[m')
        quant = float(input('Quantos kg Deseja Comprar:'))
        if(quant > 0 and quant <= 5):
            preco = quant * 6.90
            print('\033[32mQual Será A Forma De Pagamento:\033[m \n[1] - Dinheiro.\n[2] - Cartão Tabajara.')
            forma = int(input())
            if(forma == 1):
                Tp = 'Dinheiro'
                des = 0 
                Tip = 'Picanha'
            elif(forma == 2):
                Tp = 'Cartão Tabajara'
                des = preco*0.05
                final = preco - des
                Tip ='Picanha'
            print('\033[34mAguarde Um Instante Estamos Emitindo O Cupom Fiscal...\033[m')
            sleep(2)
            print('\033[34m.......\033[m')
            sleep(4)
            print('\n\n\033[32m******* CUPOM FISCAL *******\033[m')
            if(forma == 1):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,preco))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
            elif(forma == 2):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,final))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
        elif(quant > 5):
            preco = quant * 7.80
            print('\033[32mQual Será A Forma De Pagamento:\033[m \n[1] - Dinheiro.\n[2] - Cartão Tabajara.')
            forma = int(input())
            if(forma == 1):
                Tp = 'Dinheiro'
                des = 0 
                Tip = 'Picanha'
            elif(forma == 2):
                Tp = 'Cartão Tabajara'
                des = preco*0.05
                final = preco - des
                Tip ='Picanha'
            print('\033[34mAguarde Um Instante Estamos Emitindo O Cupom Fiscal...\033[m')
            sleep(2)
            print('\033[34m.......\033[m')
            sleep(4)
            print('\n\n\033[32m******* CUPOM FISCAL *******\033[m')
            if(forma == 1):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,preco))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
            elif(forma == 2):
                print('Tipo: {}\nQuantidade: {}Kg\nPreço Total: R${:.2f}\nTipo De Pagamento: {}\nValor De Desconto: R${:.2f}\nValor A Pagar: R${:.2f}'.format(Tip,quant,preco,Tp,des,final))
                print('\n\033[32m******* CUPOM FISCAL *******\033[m')
        elif(quant <=0 ):
            print('\033[34mNão É Possivel Comprar:\033[m {}Kg'.format(quant))        
else:
    print('\033[31mOpção Inválida!\033[m')