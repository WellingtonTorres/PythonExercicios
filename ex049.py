n = int(input('Digite um numero para saber a sua tabuada: '))
for c in range(1, 11):
     print('{} x {:2} = {:3}'.format(n, c, n * c))
