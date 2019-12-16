km = int(input('Quantidade Km percorrido? '))
d = float(input('Dias alugado? '))
tot = 0.15 * km + 60 * d

print('O valor total a ser pago é R${:.2f}'.format(tot))
