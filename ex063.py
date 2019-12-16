print('Sequência de Fibonacci')
print('-='*8)
qtd_termos_ = int(input('Quantos termos deseja mostrar? '))
cont_ = 0
f = 0
ant = 0
while cont_ < qtd_termos_:
    print(f, end=' - ')
    cont_ += 1
    if cont_ == 1:
        f = 1
        ant = 0
    else:
        f += ant
        ant = f - ant
print('FIM')
