dados = dict()
gols = list()
dados['nome'] = str(input('Nome jogador: '))
n_partidas = int(input('Quantas partidas jogou?'))
for i in range(0, n_partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print(dados)
