# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
# a números inteiros positivos e menores que 16.
result = 1
cont = 1
while True:
    num = int (input('Digite Um Número Inteiro, Positivo e Menor 16 E Veja o Resultado Fatorial: '))
    while(num < 0 or num > 16):
        print('\033[31mValor Inválido!\033[m')
        num = int (input('Digite Um Número Inteiro, Positivo e Menor 16 E Veja o Resultado Fatorial: '))
    if(num >= 1 and num <= 16):
        while(cont <= num):
            result = result * cont
            cont = cont + 1 
        print(result)
    esc = str(input('Deseja Continuar ? [S/N]').upper())
    if(esc == 'N'):
        break
