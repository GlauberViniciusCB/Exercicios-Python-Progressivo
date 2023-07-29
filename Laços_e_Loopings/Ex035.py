# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 
# 1 e um número inteiro informado pelo usuário.
primo = [2] 
num = int(input('Infome Um Número: '))

for i in range(3,num + 1):
    cont = 0
    for j in range(1,i + 1):
        if(i % j == 0):
            cont = cont + 1
    if (cont == 2):
        primo.append(i)
print(primo)