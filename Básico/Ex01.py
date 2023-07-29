#  Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo.
import math
raio = float(input('\n\033[33mInforme  O Raio Do Circulo: \033[m'))
final = math.pi * (raio**2)
print('\033[32mA Area Do Circulo É:\033[m {:.2f} m²'.format(final) )
