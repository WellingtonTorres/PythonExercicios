lista_ = []
par_ = []
impar_ = []
while True:
    lista_.append(int(input('Digite um valor: ')))
    break_ = str(input('Deseja parar? [S/N]')).strip().upper()
    while break_ not in 'SN':
        break_ = str(input('Digite S ou N, tente novamente!'))
    if break_ == 'S':
        break
for pos, valor_ in enumerate(lista_):
    if valor_ % 2 == 0:
        par_.append(valor_)
    elif valor_ % 2 == 1:
        impar_.append(valor_)
print(f'A lista completa é {lista_}')
print(f'A lista ímpar é {impar_}')
print(f'A lista par é {par_}')
