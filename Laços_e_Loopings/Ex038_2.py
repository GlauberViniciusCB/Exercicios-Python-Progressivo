# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
  # A - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
  # B - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
  # C - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que 
# o usuário digite o salário inicial do funcionário. 
from datetime import date

salario = int(input('Informe O Seu Salário Atual'))
ano_atual = date.today().year 
ano_inicial = 1997
salariofim = 0
porc = 0.015
while(ano_inicial <= ano_atual ):
    porc = porc *2
    salariofim = salario+(salario * porc)     
    ano_inicial = ano_inicial + 1 
print(f'No Ano De {ano_atual} Seu Salário Será De: {salariofim:.2f}')