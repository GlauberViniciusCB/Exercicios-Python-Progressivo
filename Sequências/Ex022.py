# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um 
# levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se 
# encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
# indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito: necessita da
# esfera; necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual 
# a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%
info = ['Necessita Da Esfera','Necessita De Limpeza','Necessita Troca Do Cabo Ou Conector','Quebrado Ou Inutilizado']
total = 0
guarda = 4*[0]
quant = int(input('Quantos Mouses Você Separou Para Analisar ? ')) 
for indice in range (quant):
    print('''
    Situação  

1- Necessita Da Esfera 
2- Necessita De Limpeza
3- Necessita Troca Do Cabo Ou Conector
4- Quebrado Ou Inutilizado 
    ''')
    vale = True
    while vale:
        esc = int(input(f'Qual A Situação Do Mouse {indice+1} ? ')) 
        if(esc == 1 or esc == 2 or esc == 3 or esc == 4):
            vale = False
        else:
            print('Opção Inválida!')
    guarda[esc - 1] = guarda[esc - 1] + 1

print('Situação                 Quantidade    Percentual')
for indice in range(len(info)):
    print(f'{indice+1}- {info[indice]} "   "{guarda[indice]}"   "{(guarda[indice]*100)/quant:.2f}%' )