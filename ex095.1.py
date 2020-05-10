dados = dict()
gols = list()
time = list()
while True:
    dados['jogador'] = str(input('Nome do jogador: '))
    num_ = int(input('Numero de partidas que o jogador jogou: '))
    for n in range(0, num_):
        gols.append(int(input(f'     Qunatos gols na partida {n+1}? ')))
    dados['gols'] = gols[:]  # Não esquecer de realizar cópia
    dados['total'] = sum(gols)
    dict_copy = dados.copy()
    time.append(dict_copy)
    del gols[:]
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opc in 'SN':
            break
        print('ERRO! Digite apenas S - Sim ou N - Não!')
    if opc == 'N':
        break
print('=-=' * 22)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    mostra_jog = int(input('Mostrar dados de qual jogador? (999 para): '))
    if mostra_jog == 999:
        print('====*FIM DO PROGRAMA*====')
        break
    elif 0 <= mostra_jog <= len(time)-1:
        print(f'{"LEVANTAMENTO DO JOGADOR":<25}{time[mostra_jog]["jogador"]:12}')
        for p, k in enumerate(time[mostra_jog]["gols"]):
            print(f'    No jogo {p+1} fez {k} gols.')
        print('-' * 36)
    else:
        print('NÃO EXISTE O CÓDIGO INFORMADO!')
