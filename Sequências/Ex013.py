# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a 
# média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o 
# mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp= []
for i in range (12):
    temp.append(float(input(f'Informe A Temperatuda Do Mês {i}: ')))
media = sum(temp)/len(temp)
print(f'A Média De Temperatura Anual Foi De {media}')
print('Os Meses Em Que A Temperatura Foi Abaixo Da Média Anual: ')
for i in range(12):
    if(temp[i] < media):
        print(f'O Mês {meses[i]} Teve Temperatura {temp[i]}')