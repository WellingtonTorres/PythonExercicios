fatorial_ = int(input('Digite um numero para saber seu fatorial: '))
fatorial_prox_ = fatorial_
print('Calculando {}!'.format(fatorial_))
while fatorial_prox_ != 1:
    fatorial_prox_ -= 1
    fatorial_ = fatorial_ * fatorial_prox_
print(fatorial_)
