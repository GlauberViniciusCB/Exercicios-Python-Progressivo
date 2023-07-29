# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

num1 = int(input('Informe Um Número Para A Base: '))
num2 = int(input('Informe Um Número Para O Expoente: '))
cont = 0
pot = 1
while(cont < num2):
    pot = pot * num1
    cont = cont + 1 
print(f'Base {num1} Com Expoente {num2}  Resulta Em = {pot}')
