# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com 
# um  litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 
# quilômetros 
# e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. 
# O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a
# cada execução do programa. Comparativo de Consumo de Combustível.

modelo = []
consumo = []

for i in range (0,5):
    print(f'Carro {i+1}')
    modelo.append(str(input('Modelo: ')).capitalize())
    consumo.append(float(input('Quantos Km Faz Por Litro: ')))
for i in range (0,5):
    print(f'Carro {i+1}')
    print(f'Modelo: {modelo[i]}')
    print(f'Km Por Litro: {consumo[i]}')
    print('---//---')
print('\nRELATÓRIO FINAL')
for i in range (0,5):
    print(f'{i+1} - {modelo[i]} - {consumo[i]} - {1000/consumo[i]:.2f} Litros - R${(1000/consumo[i])*2.25:.2f}')
eco = max(consumo)
pos = consumo.index(eco)
print(f'\nO Modelo Mais Econômico É: {modelo[pos]}')
