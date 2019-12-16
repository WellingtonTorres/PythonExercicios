#070 - Estatísticas em produtos
total_compra_ = cont_prod_ = cont_menor_= 0
while True:
    cont_menor_ += 1
    produto_ = str(input('Nome do produto: '))
    preco_ = float(input('Preço: R$'))
    total_compra_ += preco_
    if preco_ > 1000:
       cont_prod_ += 1
    if cont_menor_ == 1 or preco_ < menor_preco:
        menor_preco = preco_
        menor_prod = produto_
    request_ = ' '
    while request_ not in 'SN':
        request_ = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if request_ == 'N':
        print('FIM PROGRAMA')
        break
print(f'O total da compra foi de R${total_compra_:.2f}')
print(f'Temos {cont_prod_} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor_prod} custando R${menor_preco:.2f}')
