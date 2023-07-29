#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;

print('\n')
lado1 = float (input('Informe O Valor Do 1° Lado: '))
lado2 = float (input('Informe O Valor Do 2° Lado: '))
lado3 = float (input('Informe O Valor Do 3° Lado: '))

if(lado1 + lado2 > lado3 ) and (lado1 + lado3 > lado2  ) and (lado2 + lado3 > lado1 ):
    print('\nFormam Um Triângulo.')
    if(lado1 == lado2) and (lado1 == lado3):
        print('De Tipo Equilátero.')
    elif(lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
        print('De Tipo Escaleno.')
    else:
        print('De Tipo Isósceles')
else:
        print('Não Formam Um Triângulo ')
