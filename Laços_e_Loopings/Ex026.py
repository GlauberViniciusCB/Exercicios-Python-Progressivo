# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
# e ao final mostrar o número de votos de cada candidato.
cont_voto1 = 0
cont_voto2 = 0
cont_voto3 = 0
eleitores = int(input('Informe O Número Total De Eleitores: '))
i = 1
while(i <= eleitores):
    voto = int(input(f'Eleitor {i} Em Qual Candidato Você Deseja Votar:\n[1] - Candidato 1\n[2] - Candidato 2\n[3] - Candidato 3\n'))
    if(voto > 3 or voto <= 0):
        print('\033[31mVoto Inválido!\033[m')
        voto = int(input(f'Eleitor {i} Em Qual Candidato Você Deseja Votar:\n[1] - Candidato 1\n[2] - Candidato 2\n[3] - Candidato 3\n'))
        while(voto > 3 or voto <= 0):
            print('\033[31mO Voto Contínua Inválido!\033[m')
            voto = int(input(f'Eleitor {i} Em Qual Candidato Você Deseja Votar:\n[1] - Candidato 1\n[2] - Candidato 2\n[3] - Candidato 3\n'))
    if(voto == 1):
        cont_voto1 = cont_voto1 + 1 
    if(voto == 2 ):
        cont_voto2 = cont_voto2 + 1  
    if(voto == 3 ):
        cont_voto3 = cont_voto3 + 1 
    i = i + 1
print(f'O Candidato 1 Recebeu: {cont_voto1} Voto(s)')
print(f'O Candidato 2 Recebeu: {cont_voto2} Voto(s)')
print(f'O Candidato 3 Recebeu: {cont_voto3} Voto(s)')