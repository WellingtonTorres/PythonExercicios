temp_ = list()
dados = list()
pessoas_mai = []
pessoas_men = []
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
for p in dados:
    if p[1] >= maior_p:
        maior_p = p[1]
        if maior_p == p[1]:
            pessoas_mai.append(p[0])
    if menor_p == 0:
        menor_p = maior_p
    elif p[1] <= menor_p:
        menor_p = p[1]
        if menor_p == p[1]:
            pessoas_men.append(p[0])
print(f'Ao todo você cadastrou {i} pessoas.')
print(f'O maior peso foi de {maior_p:.2f}Kg. Peso de: {pessoas_mai}')
print(f'O menor peso foi de {menor_p:.2f}Kg. Peso de: {pessoas_men}')
