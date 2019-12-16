'''num = int(input('Informe um numero: '))
print('Analysing the number {}'.format(num))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))

peso = float(input('Qual é seu peso?'))
preço = 100
preço += preço * 35 / 100
print(preço)'''
frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())