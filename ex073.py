times_ = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético Mineiro', 'Botafogo',
          'Goiás', 'São Paulo', 'Grêmio', 'Bahia', 'Fortaleza',
          'Corinthians', 'Athletico-PR', 'Ceará', 'Vasco da Gama',
          'Fluminense', 'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')
print(f'Lista de times no Brasileirão {times_}')
print(f'Os cinco primeiros são: {times_[0:5]}')
print(f'Os quatos ultimos são: {times_[-4:20]}')
print(f'Times em ordem alfabética: {sorted(times_)}')
for pos, time_selc_ in enumerate(times_):
    if time_selc_ == 'Chapecoense':
        break
print(f'A {time_selc_} está na {pos+1}ª posição.')
#print(f'A Chapecoense esta na {times_.index("Chapecoense")+1}ª posição.')
