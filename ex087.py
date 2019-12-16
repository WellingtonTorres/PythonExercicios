matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_terc_col = maior_valor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
           soma_terc_col += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior_valor:
                maior_valor = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos numeros pares é: {soma_par}')
print(f'A soma da terceira coluna é: {soma_terc_col}')
print(f'O maior valor da segunda linha é: {maior_valor}')
