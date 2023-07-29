# A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script em Python que simule 1 milhão de lançamentos
# de dados e mostre a frequência que deu para cada número.
from random import randint
def Frequencia():
    print()
    for num in range(1,7):
        print(f'O Número {num} Foi Sorteado {dado.count(num)} Vezes.')

dado = []
i = 1
while(i <= 1000000):
    dado.append(randint(1,6))
    i = i+1
Frequencia()

