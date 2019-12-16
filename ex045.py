from time import sleep
from random import choice
itens = ('Pedra', 'Papel', 'Tesoura')
print(''' Sua Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
escolha = int(input('Qual é a sua jogada? '))
print('\033[1mJO\033[m')
sleep(0.5)
print('\033[1mKEN\033[m')
sleep(0.5)
print('\033[1mPO\033[m')
sleep(0.5)
jogador = itens[escolha]
computador = choice(itens)
print('=-=' * 9)
print('''O jogador escolheu {}
O computador escolheu {}'''.format(jogador, computador))
print('=-=' * 9)
if jogador == computador:
    print('EMPATE')
elif jogador == 'Pedra' and computador == 'Tesoura' or jogador == 'Papel' and computador == 'Pedra' or jogador == 'Tesoura' and computador == 'Papel':
    print('JOGADOR VENCEU!')
else:
    print('COMPUTADOR VENCEU!')
