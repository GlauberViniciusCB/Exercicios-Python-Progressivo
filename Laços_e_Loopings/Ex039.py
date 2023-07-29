# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo 
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais 
# alto e o número do aluno mais baixo, junto com suas alturas.
cont = 0
mais_alto = 0
mais_baixo = 0 
aluno_codigoMA = 0
aluno_codigoMB = 0
for cont in range (1,10):
    num_aluno = int(input(f'Informe O Número Do {cont}° Aluno: '))
    altura = float(input(f'Informe A Altura Do {cont}° Aluno:'))
    if(cont == 1):
        mais_alto = altura
        mais_baixo = altura
    else:
        if(altura > mais_alto):
            mais_alto = altura
            aluno_codigoMA = num_aluno
        if(altura < mais_baixo):
            mais_baixo = altura
            aluno_codigoMB = num_aluno
print('\n')
print(f'O Aluno Mais Alto Tem O Código {aluno_codigoMA} E Sua Altura É De {mais_alto}')
print(f'O Aluno Mais Baixo Tem O Código {aluno_codigoMB} E Sua Altura É De {mais_baixo}')        