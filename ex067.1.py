#067 - Tabuada v3.0
while True:
    valor_ = int(input('Quer ver a tabuada de qual valor? '))
    if valor_ < 0:
        break
    for cont_ in range(1, 11):
        print(f'{valor_} x {cont_:2} = {(valor_ * cont_):3}')
print('Tabuada Finalizada')