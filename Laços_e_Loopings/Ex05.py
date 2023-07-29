# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a 
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas 
# de crescimento.
# Altere o programa  permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a 
# entrada e permita repetir a operação.
cont = 0
while True:
    pais_1 = int(input('Informe A Polulação Do 1° País: '))
    taxa_1 = float(input('Qual A Taxa De Crescimento Populacional Do 1° País: '))
    pais_2 = int(input('Informe A População Do 2° País: ')) 
    while(pais_1 > pais_2):
        print(f'Informação Inválida, Por Favor Digite Uma Taxa Maior Para O 2° País.')
        pais_2 = int(input('Informe A População Do 2° País: '))
    taxa_2 = float(input('Qual A Taxa De Crescimento Populacional Do 2° País: '))
    while(pais_1 < pais_2):
        pais_1 = pais_1 + (pais_1 * taxa_1)
        pais_2 = pais_2 + (pais_1 * taxa_2)
        cont = cont + 1 
    print(f'1{pais_1} e 2{pais_2}')
    print(f'Será Necessario {cont} Anos Para Ultrapassar.')
    esc = str(input('Deseja Continuar [S/N]: ')).upper()
    while(esc != 'S' and esc != 'N' ):
        print('Opção Inválida, Tente Novamente!')
        esc= str(input('Deseja Continuar [S/N]: ')).upper()
    if(esc == 'N'):
        break
