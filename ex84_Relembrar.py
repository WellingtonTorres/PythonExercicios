temp = []
principal = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:]) #Utilizado para fazer cópia [:] sem ele cria-se uma ligação
    temp.clear()
    resp = str(input('Deseja continuar? S/N: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Pedo de: ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end=', ')
print(f'\nO menor peso foi de {menor}Kg Peso de: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end=', ')