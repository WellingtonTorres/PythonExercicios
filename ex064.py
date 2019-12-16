#Tratando Varios Valores
cont = result_ = 0
validador_ = False
while not validador_:
    valor_ = int(input('Digite um numero: '))
    if valor_ == 999:
        validador_ = True
    else:
        result_ += valor_
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, result_))

