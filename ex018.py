import math
angulo = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O ângulo {:.2f} tem o SENO de {:.2f}'.format(angulo, sen))
print('O ângulo {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tang))
