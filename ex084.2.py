temp_ = list()
dados = list()
while True:
    temp_.append(str(input('Nome: ')))
    temp_.append(int(input('Peso: ')))
    if len(dados) == 0:
        maior_p = menor_p = temp_[1]
    else:
        if temp_[1] > maior_p:
            maior_p = temp_[1]
        if temp_[1] < menor_p:
            menor_p = temp_[1]
    dados.append(temp_[:])
    temp_.clear()
    continuar_ = str(input('Deseja continuar? [S/N]')).upper()
    if continuar_ == 'N':
        break
    else:
        continue
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi {maior_p:.2f}Kg. De ', end='')
for p in dados:
    if p[1] == maior_p:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi {menor_p:.2f}Kg. De ', end='')
for p in dados:
    if p[1] == menor_p:
        print(f'{p[0]} ', end='')
