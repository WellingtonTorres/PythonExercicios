from random import randint
n_aleatorio_ = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
print(f'Os valores sorteados foram {sorted(n_aleatorio_)}')
print(f'O maior valor sorteado foi {max(n_aleatorio_)}')
print(f'O menor valor sorteado foi {min(n_aleatorio_)}')
