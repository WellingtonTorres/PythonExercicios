import math
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))
result = math.sqrt((catop ** 2 + catad ** 2 ))
print('A hipotenusa medirá: {:.2f}'.format(result))
#Simplificado
resultdefault = math.hypot(catop, catad)
print(resultdefault)
