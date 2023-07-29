# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa 
# deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o 
# funcionamento, o estilo e o número de testes (divisões) executados.
i = 1  
cont = 0
total= 0
du= [] 
n = int(input('Informe Um Número: '))
while(i <= n):
   if(i % 2 == 1 ) and (i!=2):
        du.append(i)
        cont = cont + 1
else:
        cont = cont +1 
print(du)
print(cont)