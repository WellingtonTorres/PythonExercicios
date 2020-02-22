cadastro = dict()
dados = list()
soma = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        sx = str(input('Sexo [M/F]: '))
        if sx in 'mMfF':
            cadastro['sexo'] = sx.upper()
            break
        else:
            print('ERRO! Digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    dados.append(cadastro.copy())
    parar = str(input('Deseja continuar? [S/N]'))
    if parar in 'nN':
        break
print(f'A) Ao todos temos {len(dados)} pessoas cadastradas')
for c in range(0, len(dados)):
    soma += dados[c]["idade"]
media = soma / len(dados)
print(f'B) A média de idade é de {media:.2f}')
print('C) As mulheres cadastradas foram: ', end='')
for pos, val in enumerate(dados):
    if dados[pos]["sexo"] in 'fF':
        print(f'{dados[pos]["nome"]}', end=', ')
print(' ')
print('D) Lista das pessoas que estão acima da média:')
for e in dados:
    for k, v in e.items():
        if e["idade"] > media:
            print(f'{k} = {v}; ', end=' ')
    print('')
print('<<ENCERRADO>>')
