# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o
# número de alunos com média maior ou igual a 7.0.
turma = []
alunos = {}
cont = 0
for aluno in range (10):
    media = 0
    notas = []
    alunos.clear()
    alunos['Nome'] = str(input('Digite O Nome: '))
    i= 1
    while(i <= 4):
        nota = float(input(f'Nota {i}: '))
        notas.append(nota)
        alunos['Notas']= notas
        media = sum(alunos['Notas'])
        media = media/4
        alunos['Media']= media
        if(alunos['Media']>=7):
            cont = cont + 1     
        i= i + 1
    turma.append(alunos.copy())

for i in turma:
    print(i)
print(f'O Total De  Alunos Com Média Superior A 7.0 É De: {cont} ')