# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#             Até 5 Kg           Acima de 5 Kg
# Morango   R$ 2,50 por Kg      R$ 2,20 por Kg
# Maçã      R$ 1,80 por Kg      R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
from time import sleep
total_kg = 0
preco = 0
total_ma = 0
total_mo = 0
print('=*=*'*39)
qt_morango = float(input('\033[33mQuantos Kg De Morango Você Deseja Comprar?\033[m ')) 
print('=*=*'*39)
qt_maca    = float(input('\033[33mQuantos Kg De Maça Você Deseja Comprar?\033[m '))
print('=*=*'*39)

if(qt_morango <= 5 and qt_morango > 0):
    pt = 2.50 * qt_morango
    total_mo = pt 
elif(qt_morango > 5):
    pt = 2.20 * qt_morango
    total_mo = pt
elif(qt_morango < 0):
    total_mo = 0
    print('\033[31mNão É Possivel Comprar: \033[m{} \033[31mMorango(s).\033[m'.format(qt_morango))

if(qt_maca <= 5 and qt_maca > 0):
    pt = 1.80 * qt_maca
    total_ma = pt
elif(qt_maca > 5):
    pt = 1.50 * qt_maca
    total_ma = pt
elif(qt_maca < 0):
    total_ma = 0
    print('\033[31mNão É Possivel Comprar: \033[m{} \033[31mMaça(s).\033[m'.format(qt_maca))

total_kg = qt_morango + qt_maca
preco = total_mo + total_ma
if(total_kg != 0):
    if(qt_morango <= 0):
        print('\033[34mNão Quero Comprar Morangos No Momento!\033[m') 
        total_kg = qt_morango + qt_maca
        preco = total_mo + total_ma   
    if(qt_maca <= 0):
        print('\033[34mNão Quero Comprar Maças No Momento!\033[m') 
        total_kg = qt_morango + qt_maca
        preco = total_mo + total_ma            
else:
     print('\033[34mMuito Obrigado, Não Quero Comprar Nada No Momento!\033[m')  


if(total_kg > 8 or preco > 25):
    print('\033[32mOk, Espere Um Momento, Estou Calculando!...\033[m')
    sleep(5)
    semdesc =preco
    desc = preco * 0.10
    desc = preco - desc 
    print('Peso Total: {} Kg'.format(total_kg))
    print('Preço Sem Desconto: R${:.2f}'.format(semdesc))
    print('Preço Total Com Desconto: R${:.2f}'.format(desc))
elif(total_kg == 0 and preco == 0):
   print('\033[32mOk, Até A Proxima!\033[m')
else:
    print('\033[32mOk, Espere Um Momento, Estou Calculando!...\033[m')
    sleep(5)
    semdesc = preco
    print('Peso Total: {} Kg'.format(total_kg))
    print('Preço Total: R${:.2f}'.format(semdesc))