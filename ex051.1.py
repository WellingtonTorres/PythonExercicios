print('10 TERMOS DE UMA PA')
primeiroTermo_ = int(input('Primeiro termo: '))
razao_ = int(input('Razão: '))
decimo_ = primeiroTermo_ + (10 - 1) * razao_
for c in range(primeiroTermo_, decimo_ + razao_, razao_):
    print('{}'.format(c), end='-> ')
print('ACABOU')