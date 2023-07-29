#  Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input('Informe Um Dia: '))
mes = int(input('Informe Um Mês: '))
ano = int(input('Informe Um Ano: '))
if(dia < 1 or dia > 31) or (mes < 1 or mes > 12) or (dia == 0 or mes == 0): 
     print('\033[31mData Inválida!\033[m')
elif( mes == 2 and dia > 28):
    if(mes == 2 and dia == 29 ) and ( ano % 4 != 0 and ano % 100 == 0 or ano % 400 != 0): 
        print('\033[31mData Inválida!\033[m')
        print('\033[33mEste Dia Não Existiu!\033[m')
    elif(mes == 2 and dia == 29) and(ano %4 == 0 and ano % 100 != 100 or ano % 400 == 0) :
        print('\033[32mData Válida!\033[m')
        print('\033[33mO Ano É Bissexto!\033[m')
        print('{}/{}/{}'.format(dia,mes,ano))
    else:
        print('\033[31mData Inválida!\033[m')
        print('\033[33mEste Dia Não Existiu!\033[m')
elif(mes == 1 and dia <=31 ) or (mes == 3 and dia <= 31) or (mes == 5 and dia <= 31) or (mes == 7 and dia <= 31) or (mes == 8 and dia <= 31) or (mes == 10 and dia <= 31) or (mes == 12 and dia <= 31): 
    print('\033[32mData Válida!\033[m')
    print('{}/{}/{}'.format(dia,mes,ano))
else:
    print('\033[32mData Válida!\033[m')
    print('{}/{}/{}'.format(dia,mes,ano))