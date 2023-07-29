# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
# pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
# pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando 
# não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
atleta = {}
saltos = []
media = 0
atleta['Nome'] = str(input('Informe O Nome: ')) 
if( len(atleta['Nome']) == 0):
    print('Programa Finalizado.')
else:
    for i in range (1,6):
        salto = float(input(f'{i}° Salto: '))
        saltos.append(salto)
    atleta['Salto'] = saltos
    print('\n')
    print(f'Atleta: {atleta["Nome"]}')
    for i,salto in enumerate(saltos):
        print(f'O {i+1}° Salto: {salto} m')
    print('\n')
    print('Resultado Final:')
    print(f'Atleta: {atleta["Nome"]}')
    print('Saltos:',end= ' ')
    saltos.sort(reverse = True)
    for i,salto in enumerate (saltos):
            if(i < 4):
             print(f'{salto}',end =' - ')  
            else:
                print(f'{salto}', end = '')
media = sum(saltos)/len(saltos)
print(f'\nMédia Dos Saltos: {media} m')