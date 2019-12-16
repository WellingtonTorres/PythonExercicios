v_peso = float(input('Qual é o seu peso? '))
v_altura = float(input('Qual é a sua altura? '))
imc = v_peso / v_altura ** 2
print('Seu IMC é {:.2f} e está '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc <= 25:
    print('PESO NORMAL!')
elif imc <= 30:
    print('SOBREPESO!')
elif imc <= 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MORBIDA!')