# Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que recebe um 
# inteiro n e mostra todos os primos, de 1 até n.
def Primo(n):
    cont = 0
    if(n == 1):
        print(f'O Número {n} Não É Primo.')
    else:
        for i in range(1,10):
            if(n % i == 0):
                cont= cont +1
        if(cont > 2):
            print(f'O Número {n} Não É Primo.')
        else:
            print(f'O Número {n} É Primo.')

while True:
    n = str(input('Digite Um Número Inteiro Positivo: '))
    try:
        if(n.isnumeric () and n > 0):
            numero = int(n)
            Primo(numero)
            break
    except(ValueError,TypeError):
        while(not n.isnumeric() and  n > 0):
            n = str(input('Tente Novamente, Digite Um Número Inteiro Positivo: '))
        if(n.isnumeric):
            numero = int(n)
            Primo(numero)
            break

        
     