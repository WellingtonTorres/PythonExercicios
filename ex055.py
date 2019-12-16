maiorPeso = 0
menorPeso = 0
for pessoa in range(5):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa + 1)))
    if pessoa == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('O maior peso lido foi {}Kg'.format(maiorPeso))
print('O menor peso lido foi {}Kg'.format(menorPeso))
