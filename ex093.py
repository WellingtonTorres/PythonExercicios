dados = dict()
rounds = list()
dados['nome'] = str(input('Nome jogador: '))
n_partidas = int(input('    Quantas partidas jogou?'))
for i in range(0, n_partidas):
    rounds.append(int(input(f'    Quantos gols na partida {i}? ')))
dados['gols'] = rounds[:] #Ajusteo a cópia da lista
dados['total'] = sum(rounds)
print('=' * 40)
print(dados)
print('=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 40)
print(f'O Jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for pos, val in enumerate(rounds):
    print(f'    => Na partida {pos}, fez {val} gol(s).')
print(f'Foi um total de {dados["total"]} gols.')
