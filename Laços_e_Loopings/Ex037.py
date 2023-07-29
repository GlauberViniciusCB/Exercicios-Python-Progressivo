# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
# magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e 
# seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o 
# programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais 
# magro, além da média das alturas e dos pesos dos clientes.
mais_alto = 0
mais_baixo = 0
mais_gordo = 0
mais_magro = 0  
cont = 0
matricA = 0 
matricB = 0
matricG = 0
matricM = 0
while True: 
    codigo = int(input('Informe O Seu Código De Matrícula: '))
    if(codigo == 0):
        print(f'O Mais Alto Tem {mais_alto} M Do Código {matricA} ')
        print(f'O Mais Baixo Tem {mais_baixo} M Do Código {matricB}')
        print(f'O Mais Gordo Tem {mais_gordo} Kg Do Código {matricG}')
        print(f'O Mais Magro Tem {mais_magro} Kg Do Código {matricM}')
        break
    altura = float(input('Informe Sua Altura: '))
    peso   = float(input('Informe Seu Peso: '))
    cont = cont + 1 
    if(cont == 1):
        mais_alto = altura
        mais_baixo = altura
        mais_gordo = peso
        mais_magro = peso 
    else:
        if(altura > mais_alto):
            mais_alto = altura
            matricA = codigo
        if(altura < mais_baixo):
            mais_baixo = altura
            matricB = codigo
        if(peso > mais_gordo):
            mais_gordo = peso
            matricG = codigo
        if(peso < mais_magro):
            mais_magro = peso
            matricM = codigo 

