def fatorial(n, show=False):
    '''
    => Calcula o Fatorial de um numero
    :param n: O numero a ser calculado.
    :param show: (opcional) mostra ou não a expressão.
    :return: O Valor do Fatorial de um número n.
    '''
    f = 1
    for p in range(n, 0, -1):
        if show:
            print(f'{p}', end=' ')
            if p > 1:
                print(f'x', end=' ')
            else:
                print('=', end=' ')
        f *= p
    return f


print(fatorial(10, True))
#help(fatorial)