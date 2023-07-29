# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar 
# numeros aleatórios, simulando os lançamentos dos dados.
from random import randint
valores = []
i = 1
while (i <= 100):
    dado = (randint(1,6))
    valores.append(dado)
    i = i + 1
print(valores)
print(len(valores))
for i in range (1,7):
    if(valores.count(i)):
        print(f'O Valor {i} Apareceu {valores.count(i)} Vezes.')