dist = int(input('Qual a distância da sua viagem em Km? '))
'''
if dist > 200:
    result = dist * 0.45
else:
    result = dist * 0.50
'''
result = dist * 0.50 if dist <= 200 else dist * 0.45

print('O preço da passagem é R${:.2f}'.format(result))
