import random
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores da lista!', end=' ')
    for p in range(0, 5):
        lista.append(random.randint(0, 100))
        sleep(0.3)
        print(f'{lista[p]}', end=' ')
    print('PRONTO!')


def somaPar(lista):
    sumPar = 0
    for p in lista:
        if p % 2 == 0:
            sumPar += p
    print(f'Somandos os valores paredes de {lista}, temos {sumPar}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
