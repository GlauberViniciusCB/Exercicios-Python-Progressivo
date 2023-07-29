# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor
# recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas
# brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa
# (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
# salarios = []
# for i in range (3):
#     venda = float(input('Qual O valor Da Venda Bruta Deste Mês: R$ '))
#     venda = 200 + (venda * 0.09)
#     salarios.append(venda)
# # print(salarios)
# for i in salarios:
#     if(200<i>299):
        
from tabulate import tabulate
matriz = [['asfaf',21,'SSS'],['erwrw',20,'1Ss']]
print(tabulate(matriz,headers=['nome','idade','pais']))

