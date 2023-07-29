# Faça um programa que leia 5 números e informe o maior número
i = 1
maior = 0
while(i<=5):
    num = int(input(f'Informe o {i}° Número: '))
    i=i+1
    if(i == 1):
        maior = num
    else:
        if(num > maior):
            maior = num 
print(f'O Maior Número Digitado Foi: {maior} ')