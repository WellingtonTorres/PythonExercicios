matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_terc_col = maior_valor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'A soma dos numeros pares é: {soma_par}')
for l in range(0, 3):
    soma_terc_col += matriz[l][2]
print(f'A soma da terceira coluna é: {soma_terc_col}')
for c in range(0, 3):
    if c == 0:
        maior_valor = 0
    elif matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior_valor}')
