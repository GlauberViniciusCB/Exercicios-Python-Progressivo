# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
# sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito 
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Informe A 1° Nota: '))
nota2 = float(input('Informe A 2° Nota: '))
media = (nota1 + nota2)/2 

if(media >= 0.0 and media < 4.0):
    print('Sua Nota 1 É: {} Sua Nota 2 É: {} E Sua Media É: {} '.format(nota1,nota2,media))
    print('\033[33mSeu Conceito Foi "E" Você Está Reprovado!\033[m')
elif(media >= 4.0 and media < 6.0):
    print('Sua Nota 1 É: {} Sua Nota 2 É: {} E Sua Media É: {} '.format(nota1,nota2,media))
    print('\033[33mSeu Conceito Foi "D" Você Está Reprovado!\033[m')
elif(media >= 6.0 and media < 7.5):
    print('Sua Nota 1 É: {} Sua Nota 2 É: {} E Sua Media É: {} '.format(nota1,nota2,media))
    print('\033[33mSeu Conceito Foi "C" Você Está Aprovado!\033[m')
elif(media >= 7.5 and media < 9.0):
    print('Sua Nota 1 É: {} Sua Nota 2 É: {} E Sua Media É: {} '.format(nota1,nota2,media))
    print('\033[33mSeu Conceito Foi "B" Você Está Aprovado!\033[m')
elif(media >= 9.0 and media <= 10):
    print('Sua Nota 1 É: {} Sua Nota 2 É: {} E Sua Media É: {} '.format(nota1,nota2,media))
    print('\033[33mSeu Conceito Foi "A" Você Está Aprovado!\033[m')