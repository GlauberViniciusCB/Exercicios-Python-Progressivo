# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Farenheit ou 
# vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada,
# onde esse menu chama a função de conversão correta
def Grau_Celsius(Tem):
    Res = (Tem - 32)/1.8
    return print (f'{Res:.2f}°C')
def Farenheit(Tem):
    Res = 1.8 * Tem + 32
    return print(f'{Res:.2f}°F')
def Menu():
    print('---' * 10)
    print('{:^30}'.format('Menu'))
    print('---'* 10)
    print('Escolha Uma Opção Pra Conversão: ')
    print('{:<}'.format('\n1- Farenheit Para Grau Celsius.'))
    print('{:<}'.format('2- Grau Celsius Para Farenheit .'))
    print('{:<}' .format('3- Finalizar O Programa.'))
    while True:
        esc = str(input('Digite O Número De Sua Escolha: '))
        if(esc.isnumeric()):
            escolha = int(esc)
        while(escolha > 3 and escolha < 1 ):
            print('Digite Um Número Inteiro De 1 A 3')
            esc = str(input('Digite O Número De Sua Escolha: '))
        try:
            if(esc.isnumeric()):
                escolha = int(esc)
        except(ValueError,TypeError,UnboundLocalError):
            print('Por Favor Só Digite Números')
        else:
            if(escolha == 1):
                num = int(input('Digite A Temperatuda Em Farenheit: '))
                Grau_Celsius(num)
                break
            if(escolha == 2):
                num = int(input('Digite A Temperatura Em Celsius: '))
                Farenheit(num)
                break
            if(escolha == 3):
                print('\nSistema Finalizado Com Sucesso.')
                break

Menu()
