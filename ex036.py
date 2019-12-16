valorCasa = float(input('Qual o valor da casa? '))
valorSalario = float(input('Qual o seu salário? '))
qtdAnos = int(input('Em quantos anos você pretende pagar?'))

vPresta = valorCasa / (qtdAnos * 12)
parcialSal = valorSalario * 0.30

if vPresta <= parcialSal:
    print('Empréstimo concedito com sucesso! \033[3;35mParabéns\033[m')
else:
    print('Que pena, não podemos conceder o empréstimo!')
print('O valor da prestação ficou em R${:.2f} e seu salário em 30% R${:.2f}.'.format(vPresta, parcialSal))
