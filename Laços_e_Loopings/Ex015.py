# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o 
# n−ésimo termo
num = int(input('Informe O Termo Que Deseja Ver Da Sequência De Fibonacci: '))
primeiro = 1
segundo = 1
if(num == 1 or num==2):
    soma = 1
    print(soma)
else:
    cont = 3
    while(cont <= num):
        soma = primeiro + segundo
        primeiro = segundo
        segundo = soma
        cont = cont + 1 
    print(soma)

