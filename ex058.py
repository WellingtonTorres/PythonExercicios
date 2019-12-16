from time import sleep
from random import randint
print('Sou um computador...')
sleep(0.3)
print('Acabei de pensar entre um numero de 0 a 10.')
sleep(0.2)
print('Será que você consegue advinhar?')
num_pc_ = randint(0, 10)
cont_ = 1
num_jogador_ = int(input('Me diga o seu palpite? '))
while num_pc_ != num_jogador_:
    if num_pc_ > num_jogador_:
        print('Mais... tente novamente!')
    elif num_pc_ < num_jogador_:
        print('Menos... tente novamente!')
    num_jogador_ = int(input('Qual o seu palpite? '))
    cont_ += 1
print('Acertou com {} tentativas, PARABÉNS!'.format(cont_))

