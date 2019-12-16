valores_ = []
for c in range(5):
    valores_.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Você digitou os valores: {valores_}')
menor_ = min(valores_)
print(f'\nO maior valor foi {max(valores_)} nas posições: ', end='')
for pos_, valor_ in enumerate(valores_):
    if max(valores_) == valor_:
        print(f'{pos_}', end='...')
print(f'\nO menor valor foi {min(valores_)} nas posições: ', end='')
for pos_, valor_ in enumerate(valores_):
    if min(valores_) == valor_:
        print(f'{pos_}', end='...')

