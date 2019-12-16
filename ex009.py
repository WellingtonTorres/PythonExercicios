n = int(input('Digite um numero para ver sua tabuada: '))
i = 1
print('-' * 11)
while i <= 10:
    r = n * i
    print('{} x {:2} = {:3}'.format(n, i, r))
    i += 1
print('-' * 11)
