# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.
nome  = str(input('Informe Um Nome De Usuário: '))
senha = str(input('Informe Uma Senha: '))

if(nome != senha):
    print('\n\033[32mCadastro Aprovado!\033[m')
    print('Seu Usuário É: {}'.format(nome))
    print('Sua Senha É: {}'.format(senha))
else:
    print('\033[31mSenha Inválida, Por Favor Informe Uma Senha Diferente Do Usuário!\033[m')
    while(nome == senha):
        nome  = str(input('Informe Um Nome De Usuário: '))
        senha = str(input('Informe Uma Senha: '))
        if(nome == senha):
            print('\033[31mSenha Inválida, Por Favor Informe Uma Senha Diferente Do Usuário!\033[m')
        else:
            print('\n\033[32mCadastro Aprovado!\033[m')
            print('Seu Usuário É: {}'.format(nome))
            print('Sua Senha É: {}'.format(senha))