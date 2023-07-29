# Você está no Brasil, e para temperatura usamos o grau Celsius.
# Porém, quando você for contrato para trabalhar como programador Python no exterior, deverá usar graus Fahrenheit.
# Ou seja, você fornece a temperatura em graus Celsius, e seu script faz a conversão para graus Fahrenheit.

temperatura = float(input('\nInforme Uma Temperatura Em ° Celsius:'))
final = (temperatura*1.8) + 32  
print('\033[32mOs {} °C Correspondem A: {} °F \033[m'.format(temperatura,final))
