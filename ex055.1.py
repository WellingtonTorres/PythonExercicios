listPesos = []
for pessoa in range(5):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa + 1)))
    listPesos.append(peso)
maiorPeso = max(listPesos)
menorPeso = min(listPesos)
print('O maior peso lido foi {}Kg'.format(maiorPeso))
print('O menor peso lido foi {}Kg'.format(menorPeso))
