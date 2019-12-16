from time import sleep
print('=-='*10)
print('ANALISANDO UM TRIÂNGULO')
print('=-='*10)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print("Analisando se as condições foram verdadeiras...")
sleep(3)
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não pode formar um triângulo!')