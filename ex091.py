import random
from time import sleep
jogos = dict()
jogadas = list()
for c in range(0, 4):
    jogos['jogador'] = f'jogador{c+1}'
    jogos['val_dado'] = random.randint(1, 6)
    jogadas.append(jogos.copy())
    print(f'{jogadas[c]["jogador"]} tirou {jogadas[c]["val_dado"]}')
ordenar = sorted(jogadas, key=lambda k: k['val_dado'], reverse=True)
print('RANKIG DOS JOGADORES')
for i in range(0, len(ordenar)):
    print(f'{i+1}º lugar: {ordenar[i]["jogador"]} com {ordenar[i]["val_dado"]}.')
    sleep(0.4)
print(ordenar)
