fatorial_ = int(input('Digite um numero para saber o fatorial: '))
fatorial_prox = fatorial_
fatorial_final = 1
print('Calculando {}! = '.format(fatorial_), end='')
while fatorial_prox > 0:
    print('{}'.format(fatorial_prox), end='')
    print(' x ' if fatorial_prox > 1 else ' = ', end='')
    fatorial_final *= fatorial_prox
    fatorial_prox -= 1
print(fatorial_final)
