lista_ = []
while True:
    lista_.append(int(input('Digite um valor: ')))
    break_ = str(input('Deseja parar? [S/N]')).strip().upper()
    while break_ not in 'SN':
        break_ = str(input('Digite S ou N, tente novamente!'))
    if break_ == 'S':
        break
lista_.sort(reverse=True)
print(f'Você digitou {len(lista_)} elementos')
print(f'Os valores em ordem decrescente são {lista_}')
if 5 not in lista_:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 faz parte da lista!')
