# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

print('==='*46)
print('{:^150}'.format('\033[33mDigite "S" Ou "N" Para Responder As Perguntas.\033[m'))
print('==='*46)
resp = []
quest_1 = str(input("Telefonou para a vítima? [S/N] ")).upper()
resp.append(quest_1)
quest_2 = str(input("Esteve no local do crime? [S/N] ")).upper()
resp.append(quest_2)
quest_3 = str(input("Mora perto da vítima? [S/N] ")).upper()
resp.append(quest_3)
quest_4 = str(input("Devia para a vítima? [S/N] ")).upper()
resp.append(quest_4)
quest_5 = str(input("Já trabalhou com a vítima? [S/N] ")).upper()
resp.append(quest_5)
print(f'\nO Seu Depoimento Teve As Seguintes Respostas: {resp}')
sim = resp.count('S')
if(sim == 2):
    print('Você É Suspeito!')
elif(sim == 3 or  sim == 4):
    print('Você É Cúmplice!')
elif(sim == 5):
    print('Você É Assassino!')
else:
    print('Você É Inocente!')
