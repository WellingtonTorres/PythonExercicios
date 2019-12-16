print('10 TERMOS DE UMA PA')
termo_ = int(input('Primeiro termo: '))
razao_ = int(input('Razão: '))
for c in range(10):
    print('{}'.format(termo_), end='-> ')
    termo_ += razao_
print('TERMINOU')