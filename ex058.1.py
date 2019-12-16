from random import randint
print('Sou um computador...')
print('Acabei de pensar entre um numero de 0 a 10.')
print('Será que você consegue advinhar?')
num_pc_ = randint(0, 10)
cont_ = 0
acertou = False
while not acertou:
    num_jogador_ = int(input('Qual o seu palpite? '))
    cont_ += 1
    if num_pc_ == num_jogador_:
        acertou = True
    else:
        if num_pc_ > num_jogador_:
            print('Mais... tente novamente!')
        elif num_pc_ < num_jogador_:
            print('Menos... tente novamente!')
print('Acertou com {} tentativas, PARABÉNS!'.format(cont_))
