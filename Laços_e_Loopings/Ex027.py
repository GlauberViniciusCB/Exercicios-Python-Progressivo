# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade 
# de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
i = 1
media = 0 
soma = 0
quant_turma = int(input('Quantas Turmas Tem a Escola: '))
while(i <= quant_turma):
    quant_aluno = int(input(f'Qual A Quantidade De Alunos Da {i}° Turma: '))   
    if(quant_aluno > 40 or quant_aluno < 0):
        print(f'\033[31mQuantidade Inválida, A Quantidade Maxima É De 40 Alunos Por Turma.\033[m')
        quant_aluno = int(input(f'Qual A Quantidade De Alunos Da {i}° Turma: ')) 
        while(quant_aluno > 40 or quant_aluno < 0):
            print(f'\033[31mQuantidade Inválida, A Quantidade Maxima É De 40 Alunos Por Turma.\033[m')
            quant_aluno = int(input(f'Qual A Quantidade De Alunos Da {i}° Turma: ')) 
    soma = soma + quant_aluno
    i = i + 1
media = soma/quant_turma
round(media)
print(f'A Média De Alunos Em Cada Turma Da Escola É De {media}')
