# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vet = []
for u in range(10):
    letra=(str(input('Informe Uma Letra: '))).upper()
    if(letra!= 'A'and letra!='E' and letra!='I' and letra!= 'O'and letra!='U'):
        vet.append(letra)
print(f'Ao Todo São {len(vet)} Consoante(s)')
print(f'São Elas : {vet}')
