numeros_ = int(input('Digite o primeiro valor: ')), int(input('Digite outro valor: ')), \
           int(input('Digite mais um valor: ')), int(input('Digite o ultimo valor: '))
print(f'O valor 9 apareceu {numeros_.count(9)} vezes.')
if 3 in numeros_:
    print(f'O primeiro valor 3 apareceu na posição {numeros_.index(3)+1}')
else:
    print('o numero 3 não está na tupla')
print(f'Os numeros pares são ', end='')
for c in numeros_:
    if c % 2 == 0:
        print(c, end=' ')
    