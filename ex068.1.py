import random
cont = 0
parImpar = ' '
while True:
    valorJogador = int(input('Digite um valor: '))
    valorPc = random.randint(0, 10)
    valorTot = valorJogador + valorPc
    while parImpar not in 'PI': #Melhoria, não havia esse while not in
        parImpar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if valorTot % 2 == 0:
        resultParImpar = 'PAR'
    else:
        resultParImpar = 'IMPAR'
    print(f'Você jogou {valorJogador} e o computador {valorPc}. O total deu {valorTot} e é ')
    print('PAR' if valorTot % 2 == 0 else 'ÍMPAR')
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
