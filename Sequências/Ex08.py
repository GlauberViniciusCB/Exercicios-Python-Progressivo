# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a
# idade e a altura na ordem inversa a ordem lida.
altura = []
idade = []
for i in range(5):
     altura.append(float(input('Digite Uma Altura: ')))
     idade.append(int(input('Digite Uma Idade: ')))
print(altura)
print(idade)
print(f'A Ordem Inversa Do Vetor Altura: {altura[::-1]}')
print(f'A Ordem Inversa Do Vetor Idade: {idade[::-1]}')
