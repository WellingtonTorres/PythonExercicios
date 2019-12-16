lista_ = []
while True:
    valor_ = int(input('Digite um valor: '))
    if valor_ in lista_:
        print('Valor duplicado!')
    else:
        lista_.append(valor_)
        print('Valor adicionado com sucesso...')
    break_ = str(input('Deseja continuar? [S/N]')).upper().strip()
    while break_ not in 'SN':
        break_ = str(input('Informação inválida! Informar apenas S para SIM ou N para NÃO: ')).upper().strip()
    if break_ in 'N':
        break
lista_.sort()
print(f'Você digitou os valores: {lista_}')
