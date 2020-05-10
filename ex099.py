def maiorValor(* valor):
    print('=' * 30)
    print('Analisando os valores passados...')
    for p in valor:
        print(f'{p} ', end='')
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {max(valor)}.')


maiorValor(10, 3, 4, 5)
maiorValor(10, 3, 4, 5, 3, 12)
maiorValor(10, 3, 4, 5, 12, 13, 14, 15)
maiorValor(0)
