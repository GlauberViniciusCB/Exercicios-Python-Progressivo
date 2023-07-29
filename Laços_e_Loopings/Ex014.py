# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
cont = 1 
cont_par = 0
cont_imp = 0
while(cont <= 10):
    num = int(input(f'Informe Um O {cont}° Número: '))
    cont = cont +1 
    if(num % 2 == 0):
        cont_par = cont_par + 1
    else:
        cont_imp = cont_imp + 1 

print('\n')
print(f'A Quantidade De Números Pares Digitada É De: {cont_par}')
print(f'A Quantidade De Números Ímpares Digitada É De: {cont_imp}')
