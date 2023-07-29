# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
# até que o usuário informe um valor válido.
print('\n')
nota = float(input('\033[33mInforme Uma Nota: \033[m'))
while (nota <=0 or nota > 10):
    print('\033[31mValor invalido.\033[m')
    nota = float(input('\033[33mInforme Uma Nota: \033[m'))
print('\033[32mA Nota Digitada É Válida.\033[m')
