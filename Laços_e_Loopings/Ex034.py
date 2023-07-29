# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele 
# que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
#  um  número primo.
i = 1 
primo = 0
num = int (input('Informe Um Número: '))
while (i <= num):
    div = num % i
    if(div == 0):
        primo = primo + 1
    i = i + 1 
if(primo == 2):
    print('\033[32mO Número É Primo!\033[m')
else:
    print('\033[31mNão É Primo!\033[m')