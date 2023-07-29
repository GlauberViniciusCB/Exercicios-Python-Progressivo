# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de 
# valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da 
# compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para 
# então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
# a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...
i = 1
total = 0
dinheiro = 0
troco = 0
while True:
    n = float(input(f'Informe Um O Valor Do {i}° Produto, Ou Digite \033[33m0\033[m Para Fechar O Caixa: R$')) 
    total = total + n
    if(i > 0):
        print(f'Produto {i:.2f}: R$ {n:.2f}')
    i = i + 1
    if(n == 0):
        dinheiro = float(input(f'Digite O Valor Da Nota Que Pretende Quitar A Sua Compra: R$'))
        troco = dinheiro - total
        print(f'Total: {total:.2f} ')
        print(f'Dinheiro: {dinheiro:.2f}')
        print(f'Troco: {troco:.2f}')
        break