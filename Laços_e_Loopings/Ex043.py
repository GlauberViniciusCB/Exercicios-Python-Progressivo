# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
# item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser 
# encerrado.
contador = [0]*6
cardapio = ['Cachorro Quente  ','Bauru Simples  ','Bauru com ovo  ','Hambúrguer  ','Cheeseburguer  ','Refrigerante  ']
preco =[1.20,1.30,1.50,1.20,1.30,1.00]
total = 0
while True:
    print('''\033[33mEspecificação    Código     Preço\033[m   

    Cachorro Quente  100        R$ 1,20
    Bauru Simples    101        R$ 1,30
    Bauru com ovo    102        R$ 1,50
    Hambúrguer       103        R$ 1,20
    Cheeseburguer    104        R$ 1,30
    Refrigerante     105        R$ 1,00
    ''')                 
    num = int(input('Digite Um Número: '))
    while(num < 100 or num > 105):
        print('Código Inválido, Tente Novamente! ')        
        num = int(input('Digite Um Número: '))
    if(num == 100):
        contador[0] = contador[0] + 1
    if(num == 101):
        contador[1] = contador[1] + 1
    if(num == 102):
        contador[2] = contador[2] + 1
    if(num == 103):
        contador[3] = contador[3] + 1
    if(num == 104):
        contador[4] = contador[4] + 1 
    if(num == 105):
        contador[5] = contador[5] + 1   
    esc = str(input('Deseja Continuar[S/N]? ')).upper()
    while(esc != 'S' and esc !='N'):
        print('Opção Inválida, Tente Outra Vez! ')
        esc = str (input('Deseja Continuar[S/N]?')).upper()
    if(esc == 'N'):
        print('\nPedido Encerrado')
        break
print(f'{"Nota Final":^50}')
print(f'\033[33mEspecificação    Quant     Preço\033[m')   
for item in range (0,6):
    print(f"{cardapio[item]}{contador[item]:^6} R${preco[item]*contador[item]:.2f}")
    total = total + preco[item]*contador[item]
print(f'O Preço Final Da Sua Compra É: R${total:.2f}')