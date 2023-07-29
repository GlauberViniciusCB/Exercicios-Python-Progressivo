# Foram anotadas as idades e alturas de 6 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos 
# possuem altura inferior à média de altura desses alunos.
idades = [10,13,10,8,15,14]
alturas = [1.60,1.70,1.55,1.72,1.60,1.58]
media =sum(alturas)/len(alturas)
cont = 0
print(media)
for i in range (0,len(idades)):
    if(idades[i] >13 and alturas[i]< media):
        cont = cont + 1
print(cont)