dados = dict()
gols = list()
dados['jogador'] = str(input('Nome do jogador: '))
num_ = int(input('Numero de partidas que o jogador jogou: '))
for n in range(0, num_):
    gols.append(int(input(f'     Qunatos gols na partida {n}? ')))
dados['gols'] = gols[:] #Não esquecer de realizar cópia
dados['total'] = sum(gols)
print('=-=' * 30)
print(dados)
print('=-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-=' * 30)
print(f'O jogador {dados["jogador"]} jogou {len(gols)} partidas.')
for pos, v in enumerate(gols):
    print(f'    => Na partida {pos}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
