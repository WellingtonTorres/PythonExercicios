import datetime
anoNasc = int(input('Digite o ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNasc
print('Naseu em {} e tem {} anos em {}.'.format(anoNasc, idade, anoAtual))
if idade < 18:
    print('Ainda falta(m) {} ano(s) para o alistamento!'.format(18 - idade))
elif idade > 18:
    print('Passou do prazo de alistamento em {} ano(s).'.format(idade - 18))
else:
    print('\033[7;34mJá pode se alistar!\033[m')
