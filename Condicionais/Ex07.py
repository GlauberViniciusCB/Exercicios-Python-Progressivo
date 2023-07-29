# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('\nEm Qual Turno Você Estuda?')
print('\nM - Matuino \nV - Vespertino \nN - Noturno')
turno =str(input()).upper()

if(turno == 'M'):
    print('Bom Dia!')
elif(turno == 'V'):
    print('Boa Tarde!')
elif(turno == 'N'):
    print('Boa Noite!')
else:
    print('\033[31mValor Inválido!\033[m')
