# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Digite Uma Letra: ')).upper()

if(letra == 'A' or letra == 'E' or letra == 'I'or letra == 'O' or letra == 'U'):
    print('A Letra {} É Uma Vogal!'.format(letra))
else:
    print('A Letra {} É Uma Consoante!'.format(letra))
