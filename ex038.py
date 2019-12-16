n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro {}.'.format(n2, n1))
else:
    print('Não há valor maior ambos são iguais!')
