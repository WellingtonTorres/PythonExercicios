prec = float(input('Qual o preço do produto? R$ '))

desc = prec * (1 - 0.05)
print('O produto que custava R${:.2f} passa a custar com o desconto R${:.2f}'.format(prec, desc))
