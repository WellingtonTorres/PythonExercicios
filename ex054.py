from datetime import datetime
menor = 0
maior = 0
for c in range(7):
    anoNasc = int(input('Em que ano a pessoa {}ª pessoa nasceu? '.format(c+1)))
    if datetime.today().year - anoNasc >= 18:
        maior += 1
    elif datetime.today().year - anoNasc < 18:
        menor += 1
    else:
        print('Valor invalido!')
print('Ao todo tivemos {} pessoas maiores de idade \nE {} pessoas menores de idade.'.format(maior, menor))
