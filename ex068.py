#Par ou ímpar
import random
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*25)
cont = 0
while True:
    valorJogador = int(input('Digite um valor: '))
    valorPc = random.randint(0, 10)
    valorTot = valorJogador + valorPc
    parImpar = ' '
    while parImpar not in 'PI': #Melhoria, não havia esse while not in
        parImpar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if valorTot % 2 == 0:
        resultParImpar = 'PPAR'
    else:
        resultParImpar = 'IÍMPAR'
    print(f'Você jogou {valorJogador} e o computador {valorPc}. O total deu {valorTot} e é {resultParImpar[1:6]}')
    if resultParImpar[0] == parImpar:
        print('=' * 30)
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('=' * 30)
        print('VOCÊ PERDEU')
        break
print('=' * 30)
print(f'GAME OVER! Você ganhou {cont} vezes!')
