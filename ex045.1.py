from time import sleep
from random import choice
itens = ('Pedra', 'Papel', 'Tesoura')
computador = choice(itens)
print(''' Sua Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é sua jogada? '))
jogador = itens[jogador]
print('.....')
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('=-=' * 9)
print('''O jogador escolheu {}
O computador escolheu {}'''.format(jogador, computador))
print('=-=' * 9)
if computador == 'Pedra':
    if jogador == 'Pedra':
        print('EMPATE')
    elif jogador == 'Papel':
        print('JOGADOR VENCE')
    elif jogador == 'Tesoura':
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 'Papel':
    if jogador == 'Pedra':
        print('COMPUTADOR VENCE')
    elif jogador == 'Papel':
        print('EMPATE')
    elif jogador == 'Tesoura':
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 'Tesoura':
    if jogador == 'Pedra':
        print('JOGADOR VENCE')
    elif jogador == 'Papel':
        print('COMPUTADOR VENCE')
    elif jogador == 'Tesoura':
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
