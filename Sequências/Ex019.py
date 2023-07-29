# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos 
# valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num 
# vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos 
# concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
cont_voto = 0
total_votos = 0
sistemas ={'1':['Windows Server',0],'2':['Unix',0],'3':['Linux',0],'4':['Netware',0],'5':['Mac OS',0],'6':['Outros',0]} 
while True:
    print('''\nQual o melhor Sistema Operacional para uso em servidores?

        As possíveis respostas são:

        1- Windows Server
        2- Unix
        3- Linux
        4- Netware
        5- Mac OS
        6- Outro
        0- Finalize O Programa
''')    
    esc = int(input('Faça Sua Escolha: '))
    while(esc < 0 or esc > 6):
        print('Opção Inválida, Tente Novamente!')
        esc = int(input('Faça Sua Escolha: '))
    if(esc == 0):
        print('Votação Finalizada.')
        break
    if(esc == 1):
        cont_voto = sistemas['1'][1] 
        sistemas.update({'1':[sistemas['1'][0],cont_voto + 1]})
    if(esc == 2):
        cont_voto = sistemas['2'][1]
        sistemas.update({'2':[sistemas['2'][0],cont_voto + 1]})
    if(esc == 3):
        cont_voto = sistemas['3'][1]
        sistemas.update({'3':[sistemas['3'][0],cont_voto + 1]})
    if(esc == 4):
        cont_voto = sistemas['4'][1]
        sistemas.update({'4':[sistemas['4'][0],cont_voto + 1]}) 
    if(esc == 5): 
        cont_voto = sistemas['5'][1]
        sistemas.update({'5':[sistemas['5'][0],cont_voto + 1]})
    if(esc == 6):
        cont_voto = sistemas['6'][1]
        sistemas.update({'6':[sistemas['6'][0],cont_voto + 1]}) 
    if(cont_voto != '0'):
        total_votos = total_votos + 1
print(f'Sistema Operacional          Votos                     %')
for chave,valor in sistemas.items():
    print(valor[0],'              ',valor[1],'                ',valor[1]/total_votos*100)
print(f'Total De Votos:{total_votos}')