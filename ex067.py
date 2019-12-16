#067 - Tabuada v3.0
cont_ = 0
while True:
    valor_ = int(input('Quer ver a tabuada de qual valor? '))
    if valor_ < 0:
        break
    while cont_ < 10:
        cont_ += 1
        print(f'{valor_} x {cont_:2} = {(valor_ * cont_):3}')
    cont_ = 0
print('Tabuada Finalizada')