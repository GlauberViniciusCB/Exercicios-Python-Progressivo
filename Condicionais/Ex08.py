#  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para 
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário 
# atual:

#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
#     informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

print('\n')
print('\033[33m=_=' * 50,'\n{:^140}\033[33m'.format('Organizações Tabajara'))
print('\033[33m=_=\033[m'* 50)
salario_atual = float (input('\nQual O Seu Salário? '))

if(salario_atual < 280 ):
    aumento = '20%'
    ajuste = salario_atual * 0.20
    total = salario_atual + ajuste
    print('\nSalário Atual: R$',salario_atual,'\nPercentual De Aumento: R$',aumento,'\nAjuste: R$',ajuste,'\nNovo Salário: R$',total,)

elif(salario_atual >=280 and salario_atual < 700):
    aumento = '15%' 
    ajuste = salario_atual * 0.15
    total = salario_atual + ajuste
    print('\nSalário Atual: R$',salario_atual,'\nPercentual De Aumento: R$',aumento,'\nAjuste: R$',ajuste,'\nNovo Salário: R$',total,)

elif(salario_atual >= 700 and salario_atual < 1500):
    aumento = '10%'
    ajuste = salario_atual * 0.10
    total = salario_atual+ ajuste
    print('\nSalário Atual: R$',salario_atual,'\nPercentual De Aumento: R$',aumento,'\nAjuste: R$',ajuste,'\nNovo Salário: R$',total,)

else: 
    aumento = '5%'
    ajuste = salario_atual * 0.05
    total = salario_atual + ajuste 
    print('\nSalário Atual: R$',salario_atual,'\nPercentual De Aumento: R$',aumento,'\nAjuste: R$',ajuste,'\nNovo Salário: R$',total,)

