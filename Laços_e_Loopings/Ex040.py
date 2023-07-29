# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os 
# seguintes dados:
# A - Código da cidade;
# B - Número de veículos de passeio (em 1999);
# C - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# E - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# F - Qual a média de veículos nas cinco cidades juntas;
# G - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

maior = 0
menor = 0
i_maior = 0
i_menor = 0
total_m_v = 0
soma_ac = 0
cont = 0
cont_ac = 0
media_ac = 0
for i in range (1,6):
    codigo = int(input(f'Informe O Código Da {i}° Cidade: '))
    quant_vec = int(input(f'Informe A Quantidade De  Carros Da {i}° Cidade: ')) 
    total_m_v = total_m_v + quant_vec
    quant_aci = int(input(f'Informe A Quantidade De Acidentes Da {i}° Cidade: '))
    if(quant_vec < 2000):
        soma_ac = quant_aci + soma_ac
        cont_ac= cont_ac+1
    if(i == 1 ):
        maior = quant_aci
        menor =  quant_aci
        i_maior = i
        i_menor = i
    else:
        if(quant_aci > maior ):
            maior = quant_aci
            i_maior = i
        if(quant_aci < menor):
            menor = quant_aci
            i_menor = i
    cont = cont +1 
media = total_m_v/cont
media_ac = soma_ac/cont_ac 
print(f'A Maior Cidade Com Índice De Acidentes É {maior} E Pertence A Cidade {i_maior} ')
print(f'A Menor Cidade Com Índice De Acidentes É {menor} E Pertence A Cidade {i_menor} ')
print(f'A Média De Veículos Nas Cinco Cidades Juntas É De: {media}')
print(f'A Média De Acidentes De Trânsito Nas Cidades Com Menos De 2.000 Veículos De Passeio: {media_ac:.2f}')