listagem_ = ('Lápis', 1.75
             ,'Borracha', 2
             ,'Caderno', 15.90
             ,'Estojo', 25
             ,'Transferidor', 4.80)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('=' * 40)
for pos in range(0, len(listagem_)):
    if pos % 2 == 0:
        print(f'{listagem_[pos]:.<30}', end='')
    else:
        print(f'R${listagem_[pos]:>7.2f}')
