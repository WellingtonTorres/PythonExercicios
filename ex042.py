a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segemento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
     if a == b and b == c:
        print('Os segmentos formam um triangulo EQUILATERO!')
     elif a == b != c or c == a != b or c == b != a:
         print('Os segmentos formam um triangulo ISOSCELES!')
     else:
         print('Os segmentos formam um triangulo ESCALENO')
else:
    print('Os segmentos não formam um Triangulo!')
