# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for nota in range(4):
    notas.append(int(input('Informe Um Nota: ')))
print(notas)
print(f'A Média Das Notas É: {sum(notas)/4}')