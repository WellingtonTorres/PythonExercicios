import random
lista = []
x = 1
for _ in range(4):
    nomes = input('Digite o {}º nome: '.format(x))
    lista.append(nomes)
    x += 1
random.shuffle(lista)
print('A ordem de apresentão será {}.'.format(lista))
