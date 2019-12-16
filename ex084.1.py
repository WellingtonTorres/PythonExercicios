temp_ = list()
dados = list()
i = maior_p = menor_p = 0
while True:
    temp_.append(str(input('Nome: ')))
    temp_.append(int(input('Peso: ')))
    dados.append(temp_[:])
    temp_.clear()
    i += 1
    continuar_ = str(input('Deseja continuar? [S/N]')).upper()
    if continuar_ == 'N':
        break
    else:
        continue
print(f'Ao todo você cadastrou {i} pessoas.')
for p in dados:
    if p[1] >= maior_p:
        maior_p = p[1]
        if maior_p == p[1]:
            temp_.append(p[0])
print(f'O maior peso foi de {maior_p:.2f}Kg. Peso de: {temp_}')
temp_.clear()
menor_p = maior_p
for p in dados:
    if p[1] < menor_p:
        menor_p = p[1]
print(f'O menor peso foi de {menor_p:.2f}Kg. Peso de: ', end='')
for p in dados:
    if menor_p == p[1]:
        print(f'{p[0]}', end=' ')
