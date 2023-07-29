# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve 
# informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
i = 0 
num = int(input('Informe O Número Que Deseja Ver A Tabuada: '))
print('\n')
while(i <= 10):
    print(num,'X',i,'=',num*i)
    i = i + 1
