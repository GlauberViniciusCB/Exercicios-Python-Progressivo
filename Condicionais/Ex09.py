# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário 
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os 
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% 
    
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#     Salário Bruto: (5 * 220)        : R$ 1100,00
#     (-) IR (5%)                     : R$   55,00 
#     (-) INSS ( 10%)                 : R$  110,00
#     FGTS (11%)                      : R$  121,00
#     Total de descontos              : R$  165,00
#     Salário Liquido                 : R$  935,00


valor_hora = float(input('\n\033[33mInforme O Valor Do Seu Salário Por Hora:\033[m R$')) 
quant_horas = float(input('\n\033[33mInforme A Quantidade De Horas Trabalhadas:\033[m '))
salario_total= valor_hora * quant_horas
print ('\nSeu Salário É : {} '.format(salario_total))



if (salario_total < 900):
    salario_bruto = salario_total
    inss = salario_total * 0.10
    fgts = salario_total * 0.11     
    desctotal = inss + fgts 
    ir = 0

    salario_total = salario_total - inss - fgts
    print('\nSalário Bruto: R${}''\nIR: R${}''\nINSS: R${}''\nFGTS: R${}''\nTotal De Descontos: R${}''\nSeu Salario liquido É: R${} \n '. format(salario_bruto,ir,inss,fgts,desctotal,salario_total))
elif (salario_total >= 900 and  salario_total < 1500):
    salario_bruto = salario_total
    ir = salario_total * 0.05
    inss = salario_total * 0.10
    fgts = salario_total * 0.11     
    desctotal = inss + fgts + ir 

    salario_total = salario_total - inss - fgts -ir
    print('\nSalário Bruto: R${}''\nIR: R${}''\nINSS: R${}''\nFGTS: R${}''\nTotal De Descontos: R${}''\nSeu Salario liquido É: R${} \n '. format(salario_bruto,ir,inss,fgts,desctotal,salario_total))
elif (salario_total >= 1500 and  salario_total < 2500):
    salario_bruto = salario_total
    ir = salario_total * 0.10
    inss = salario_total * 0.10
    fgts = salario_total * 0.11     
    desctotal = inss + fgts + ir 

    salario_total = salario_total - inss - fgts -ir
    print('\nSalário Bruto: R${}''\nIR: R${}''\nINSS: R${}''\nFGTS: R${}''\nTotal De Descontos: R${}''\nSeu Salario liquido É: R${} \n '. format(salario_bruto,ir,inss,fgts,desctotal,salario_total))
else:
    salario_bruto = salario_total
    ir = salario_total * 0.20
    inss = salario_total * 0.10
    fgts = salario_total * 0.11     
    desctotal = inss + fgts + ir 

    salario_total = salario_total - inss - fgts -ir
    print('\nSalário Bruto: R${}''\nIR: R${}''\nINSS: R${}''\nFGTS: R${}''\nTotal De Descontos: R${}''\nSeu Salario liquido É: R${} \n '. format(salario_bruto,ir,inss,fgts,desctotal,salario_total))