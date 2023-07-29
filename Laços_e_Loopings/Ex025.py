# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma 
# varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média 
# calculada.
cont = 0
media = 0
soma = 0 
while True:
    n = int(input(f'Informe A Idade Da {cont+1}° Pessoa Ou Digite \033[33m0\033[m Para Encerrar: '))
    soma = soma + n
    if(n==0):
        media = soma/cont
        break
    cont = cont + 1
       
print(f'A Média De Idades É De: {media:.2f}')
if(media > 0 and media <=25):
    print('A Turma É Jovem!')
elif(media >= 26 and media <= 60):
    print('A Turma É Adulta!')
else:
    print('A Turma É Idosa')