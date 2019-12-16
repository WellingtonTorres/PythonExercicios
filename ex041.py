from datetime import date
anoNasc = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classsificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
