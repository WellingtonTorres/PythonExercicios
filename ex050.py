soma = 0
for c in range(6):
    n1 = int(input('Digite o {}º valor:'.format(c+1)))
    if n1 % 2 == 0:
        soma += n1
print('A soma dos numeros pares é:{}'.format(soma))
