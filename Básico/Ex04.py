# Um novo modelo de carro, super econômico foi lançado. Ele faz 20 km com 1 litro de combustível. Cada litro de 
# combustível custa R$ 5,00.
# Faça um programa que pergunte ao usuário quanto de dinheiro ele tem e em seguida diga quantos litros de combustível
# ele pode comprar e quantos kilometros o carro consegue andar com este tanto de combustível.
din = float(input('\nQuanto De Dinheiro Você Tem: R$'))
comprar = din/5
km = comprar*20
print('Você Pode Comprar {} Litros De Gasolina.'.format(comprar))
print('Será Possivel Fazer um Percurso {} Km'.format(km))