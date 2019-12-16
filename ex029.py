veloc = int(input('Qual é a velocidade do carro atual? '))
if veloc > 80:
    multa = (veloc - 80) * 7
    print('Você excedeu o limite de velocidade!\n A multa custará R${:.2f}'.format(multa))
print('A velocidade de {}Km/h está dentro do limite permitido!'.format(veloc))
