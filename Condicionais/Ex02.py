# Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte 
# resultado:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Informe A 1° Nota: '))
nota2 = float(input('Informe A 2° Nota: '))
media = (nota1 + nota2)/2
if(media >= 7 and media < 10):
    print('Sua Média é {} Aprovado!'.format(media))
elif(media < 7):
    print('Sua Média é {} Reprovado!'.format(media))
elif(media == 10):
    print('Sua Média é {} Aprovado Com Distinção!'.format(media)) 