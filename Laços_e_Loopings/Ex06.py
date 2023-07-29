# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele 
# mostre os números um ao lado do outro.
cont  = 1
cont2 = 1
print('\033[33mNúmeros De 1 A 20 Listados Um Abaixo Do Outro:\033[m')
while (cont <= 20):
    print(cont)
    cont = cont + 1
print('Fim')
print('\n\033[33mNúmeros De 1 A 20 Listados Lado A Lado Do Outro:\033[m')
while(cont2 <= 20):
    print(cont2,end =' ')
    cont2 = cont2 + 1 
print('Fim')