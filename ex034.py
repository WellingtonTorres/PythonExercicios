salario = float(input('Dgiite o salario do funcionario: R$'))
'''
if salario > 1250:
    salariofinal = salario * 1.10
if salario <= 1250:
    salariofinal = salario * 1.15
'''
if salario > 1250:
    salariofinal = salario + (salario * 10 / 100)
else:
    salariofinal = salario + (salario * 15 / 100)
print('O salario era R${:.2f} e passa ser R${:.2f}'.format(salario, salariofinal))
