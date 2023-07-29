# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de 
# quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o 
# valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na 
# tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços 
# de 1 até 50 produtos, conforme o exemplo abaixo:

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

print('*=*'*45)
print(f'                                                 Loja De Artigos: Sr. Manoel     ')
print('*=*'*45)
print('\n# Lojas Quase Dois - Tabela de preços\n')
i = 1
while(i <= 50):
    print('# {} - R$ {:.2f}'.format(i,i*1.99))
    i = i + 1
