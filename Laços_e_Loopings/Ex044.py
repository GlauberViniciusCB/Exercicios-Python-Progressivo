# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados
# são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A porcentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
candidatos = ['Jose','João','Any','Emmie','Voto Nulo','Voto em Branco']
votos = [0]*6
while True:
    print('''
    Votação Faça Sua Escolha:

    1 - Jose
    2 - João
    3 - Any
    4 - Emmie
    5 - Voto Nulo
    6 - Voto em Branco
    0 - Encerrar Votação
    ''')
    esc = int(input('Sua Escolha: '))
    while(esc < 0 or esc > 6):
        print('Opção Inválida, Tente Novamente!')
        esc = int(input('Sua Escolha: '))
    if(esc == 1):
        votos[0] = votos[0] + 1
    if(esc == 2):
        votos[1] = votos[1] + 1
    if(esc == 3):
        votos[2] = votos[2] + 1
    if(esc == 4):
        votos[3] = votos[3] + 1 
    if(esc == 5):
        votos[4] = votos[4] + 1 
    if(esc == 6):
        votos[5] = votos[5] + 1 
    if(esc == 0):
        break
print(votos)
print(sum(votos))
total = sum(votos)
print('Candidatos         Votos Computados       %')
for item in range (0,6):
    print(f'{candidatos[item]}  {votos[item]:^37}  {(votos[item]*100)/total:.2f} ')
print(votos)
print(f'Total De Votos: {sum(votos)}')