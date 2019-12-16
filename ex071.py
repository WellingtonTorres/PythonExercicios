valor_ = float(input('Valor que deseja sacar? R$'))
total_ = valor_
céd = 50
totcéd = 0
while True:
    if total_ >= céd:
        total_ -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total_ == 0:
            break
