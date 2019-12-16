lista_ = []
lista_par_ = []
lista_imp_ = []
while True:
    valor_ = int(input('Digite um valor: '))
    lista_.append(valor_)
    if valor_ % 2 == 0:
        lista_par_.append(valor_)
    else:
        lista_imp_.append(valor_)
    break_ = str(input('Deseja parar? [S/N]')).strip().upper()
    while break_ not in 'SN':
        break_ = str(input('Digite S ou N, tente novamente!'))
    if break_ == 'S':
        break
print(f'A lista completa é {lista_}')
print(f'A lista de pares é {lista_par_}')
print(f'A lista de impares é {lista_imp_}')

