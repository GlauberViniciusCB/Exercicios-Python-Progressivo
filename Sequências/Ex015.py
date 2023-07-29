# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados 
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
numeros = []
cont = 0
cont_7 = 0
while True:
    num = int(input('Informe Um Numero, Caso Queira Encerrar O Programa Digite \033[31m"-1" \033[m: '))
    if(num != -1):
        numeros.append(num)
    if(num == -1):
        print('\n\033[34mPrograma Finalizado Com Sucesso!\033[m')
        break
print(numeros)
media = sum(numeros)/len(numeros)
print(f'A Quantida De Valores Lidos Foi De {len(numeros)} Números. ')
print(f'Todos Os Valores Na Ordem Em Que Foram Digitados, Um Ao Lado Do Outro: {numeros}')
print(f'A Soma De Todos Os Números Digitados É: {sum(numeros)}')
print(f'A Média Dos Valores Digitado É: {media:.2f}')
print(f'A Quantidade De Valores Acima Da Média É De: ', end='')
for i in numeros:
    if(i > media):
        cont = cont + 1
print(cont)
print(f'A Quantidade De Valores Abaixo De Sete: ', end ='')
for i in numeros:
    if(i < 7):
        cont_7= cont_7 + 1
print(cont_7)
