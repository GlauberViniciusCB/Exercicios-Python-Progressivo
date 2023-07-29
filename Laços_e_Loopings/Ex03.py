# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = str (input('\nInforme Um Nome: ')).strip()
len(nome)
if(len(nome)< 3):
    while(len(nome)<3):
        print('\n\033[31mInformação Invalida!\033[m')
        nome = str (input('Informe Um Nome: ')).strip()
idade = int (input('\nInforme Sua Idade: '))
if(idade < 0 or idade > 150):
       while(idade < 0 or idade > 150 ):
        print('\n\033[31mInformação Invalida!\033[m')
        idade = int (input('Informe Sua Idade: '))
salario = float(input('Informe Seu Salário: R$'))
if(salario < 0):
        while (salario < 0):
            print('\n\033[31mInformação Invalida!\033[m')
            salario = float(input('\nInforme Seu Salário: R$'))
sexo = str (input('Qual O Seu Sexo:\nM - Masculino \nF - Feminino\n ')).upper()
if( sexo !='M' or sexo !='F' ):
    while(sexo != 'M' and sexo != 'F'):
       print('\n\033[31mInformação Invalida!\033[m')
       sexo = str (input('Qual O Seu Sexo:\nM - Masculino \nF - Feminino\n ')).upper()
estciv = str(input('Qual O Seu Estado Civil: \nS - Solteiro(a)\nC - Casado(a)\nV - Viúvo(a)\nD - Divorciado(a)\n')).upper()
if(estciv !='S' or estciv !='C' or estciv !='V' or estciv != 'D'):
    while(estciv !='S' and estciv !='C' and estciv !='V' and estciv != 'D'):
        print('\n\033[31mInformação Invalida!\033[m')        
        estciv = str(input('Qual O Seu Estado Civil: \nS - Solteiro(a)\nC - Casado(a)\nV - Viúvo\nD - Divorciado\n')).upper()
if(estciv =='S'):
    estciv ='Solteiro(a).'
elif(estciv =='C' ):
    estciv = 'Casado(a).'
elif(estciv =='V' ):
    estciv = 'Viúvo(a).'
elif(estciv == 'D' ):
    estciv ='Divorciado(a).'   

if(sexo == 'M' ):
    sexo = 'Masculino.'
elif(sexo == 'F'):
    sexo = 'Feminino.'
print('\n','*=*'*20,'INFORMAÇÕES PESSOAIS','*=*'*20)
print('\nNOME: {}''\nIDADE: {} Anos. \nSEXO: {}''\nSALÁRIO: R${}''\nESTADO CIVIL: {}'.format(nome,idade,sexo,salario,estciv))
print('\n','*=*'*20,'*=**=**=**=**=**=**=*','*=*'*20)