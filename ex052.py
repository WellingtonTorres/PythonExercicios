n1 = int(input('Digite um numero: '))
i = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        i += 1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n1, i))
if i == 2:
    print('Por isso é primo')
else:
    print('Por isso não é primo')
