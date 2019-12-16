from datetime import datetime
maior_ = 0
menor_ = 0
atual_ = datetime.today().year
for c in range(7):
    anoNasc = int(input('Em que ano a pessoa {}ª pessoa nasceu? '.format(c+1)))
    if atual_ - anoNasc >= 18:
        maior_ += 1
    elif atual_ - anoNasc < 18:
        menor_ += 1
    else:
        print('Valor invalido!')
print('Ao todo tivemos {} pessoas maiores de idade \nE {} pessoas menores de idade.'.format(maior_, menor_))
