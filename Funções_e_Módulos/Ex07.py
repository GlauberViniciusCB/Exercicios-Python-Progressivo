# Um número é dito perfeito quando ele é igual a soma de seus fatores. Por exemplo, os fatores de 6 são 1, 2 e 3 (ou seja,
# podemos dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que recebe um 
# inteiro e dizer se é perfeito ou não. Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.

def Perfeito(n):
    soma = 0
    for numero in range(1,n+1):
        if(n % numero  == 0):
            soma = soma + numero
        if(soma == n):
            return print(f'{n} É Um Número Perfeito.')
        else:
            return print(f'{n} Não É Um Número Perfeito.')

num = int(input('Digite Um Número Inteiro: '))
Perfeito(num)
