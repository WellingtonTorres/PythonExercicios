from time import sleep


def maiorValor(* valor):
    print('=' * 30)
    print('Analisando os valores passados...')
    c = 0
    max_v = 0
    for p in valor:
        print(f'{p} ', end='')
        sleep(0.3)
        c += 1
        if p > max_v:
            max_v = p

    print(f'Foram informados {c} valores ao todo.')
    print(f'O maior valor informado foi {max_v}.')


maiorValor(10, 3, 4, 5)
maiorValor(10, 3, 4, 5, 3, 12)
maiorValor(10, 3, 4, 5, 12, 13, 14, 15)
maiorValor(0)
