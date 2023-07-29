# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em 
# cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
i = 1
soma = 0
media = 0
p_cds = 0 
quant_cds = int(input('Quantos Cds Você Tem Na Sua Coleção: '))
for i in range (quant_cds):
    p_cds = float(input(f'Quanto Você Pagou No {i+1}° Cd: R$'))
    soma = soma + p_cds
    media = soma/quant_cds
    i = i + 1
print(f'\033[32mVocê Gastou R${soma:.2f} Em Cds E Pagou Em Média R${media:.2f} Em Cada Cd.\033[m')

