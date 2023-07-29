# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado 
# de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
cont = 0 
maior = 0
menor = 0
soma = 0
while True:
    temp = int(input(f'Informe A {cont+1}° Temperatura, Para Encerrar Digite \033[31m0\033[m: '))
    resp = str(input('Deseja Continuar? [S/N] ')).upper()
    while(resp != 'S' and resp != 'N' ):
        print('\033[31mResposta Inválida!\033[m')
        resp = str(input('Deseja Continuar? [S/N] ')).upper()
    if(cont == 1):
        maior = temp
        menor = temp  
    else: 
        if(temp > maior):
            maior = temp
        if(temp < menor):
            menor = temp 
    soma = soma + temp 
    cont = cont + 1 
    media = soma/cont
    
    print(cont)
    if(resp == 'N'):
        print('\n')
        print(f'O Menor Temperatura É: {menor}')
        print(f'O Maior Temperatura É: {maior}')
        print(f'A Média Das Temperaturas É: {media}')
        break