def fatorial(n, show=False):
    '''
    => Calcula o Fatorial de um numero
    :param n: O numero a ser calculado.
    :param show: (opcional) mostra ou não a expressão.
    :return: O Valor do Fatorial de um número n.
    '''
    f = 1
    for p in range(0, 5):
        f *= n
        n -= 1
    return f'{f}'


print(fatorial(5))
help(fatorial)