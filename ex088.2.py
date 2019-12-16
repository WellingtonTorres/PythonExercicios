from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGUE NA MEGA SENA      ')
print('-' * 30)
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(qtd_jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-=' * 3, f' SORTEANDO {qtd_jogos} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
#PROFESSOR + O MEU MELHORAMENTO