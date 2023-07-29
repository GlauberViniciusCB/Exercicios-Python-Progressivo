2# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no 
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como 
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
from time import sleep
sim = 0
nao = 0
print('=*=*'*39)
print('                                              \033[33mResponda As Questões Do Depoimento Digitando \n[1]- Sim Ou [2]- Não \033[m')
print('=*=*'*39)
q1 = int(input('\n\033[32mTelefonou Para A Vítima?\033[m\n[1]- Sim Ou [2]- Não \n'))

if(q1 == 1):
    sim = sim +1
elif(q1 == 2 or q1 == 'NÃO' ):
    nao = nao+1

if( q1 == 1):
    resp ='Sim.' 
elif(q1 == 2):
    resp = 'Não.'
print('Sua Resposta Foi: {}'.format(resp))

q2 = int(input('\n\033[32mEsteve No Local Do Crime?\033[m\n[1]- Sim Ou [2]- Não \n'))
if(q2 == 1 ):
    sim = sim +1
elif(q2 == 2 ):
    nao = nao+1

if( q2 == 1):
    resp ='Sim.' 
elif(q2 == 2):
    resp = 'Não.'
print('Sua Resposta Foi: {}'.format(resp))

q3 = int(input('\n\033[32mMora Perto Da Vítima?\033[m\n[1]- Sim Ou [2]- Não \n'))
if(q3 == 1 ):
    sim = sim +1
elif(q3 == 2 ):
    nao = nao+1

if( q3 == 1):
    resp ='Sim.' 
elif(q3 == 2):
    resp = 'Não.'
print('Sua Resposta Foi: {}'.format(resp))

q4 = int(input('\n\033[32mDevia Para A Vítima?\033[m\n[1]- Sim Ou [2]- Não \n'))
if(q4 == 1 ):
    sim = sim +1
elif(q4 == 2 ):
    nao = nao+1

if( q4 == 1):
    resp ='Sim.' 
elif(q4 == 2):
    resp = 'Não.'
print('Sua Resposta Foi: {}'.format(resp))

q5= int(input('\n\033[32mJá Trabalhou Com A Vítima?\033[m\n[1]- Sim Ou [2]- Não \n'))
if(q5 == 1 ):
    sim = sim +1
elif(q5 == 2 ):
    nao = nao+1

if( q5 == 1):
    resp ='Sim.' 
elif(q5 == 2):
    resp = 'Não.'
print('Sua Resposta Foi: {}'.format(resp))

print('\033[33m\nAnalisando...')
sleep(5)
print('\n\033[31mSim: \033[m',sim,'\n\033[32mNão: \033[m',nao)
# 2 questões ela deve ser classificada como "Suspeita"
if(sim == 2):
    print('Suspeita!')
# entre 3 e 4 como  "Cúmplice"
elif(sim >=3 and sim <=4):
    print('Cúmplice!')
# 5 como "Assassino"
elif(sim == 5):
    print('\033[31;41mAssassino!\033[m')
else:
    print('\033[32;42mInocente!\033[m')