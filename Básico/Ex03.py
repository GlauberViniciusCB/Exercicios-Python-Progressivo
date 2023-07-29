# Agora faça o contrário. Você fornece a temperatura em graus Fahrenheit, seu programa conversar para Celsius e exibe na
# tela.

temperatura = float(input('\nInforme A Temperatura Em ° Fahrenheit: '))
final = (temperatura-32)/ 1.8
print('\033[32mOs {}°F Correspondem A: {} °C \033[m'.format(temperatura,final))