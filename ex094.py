cadastro = dict()
dados = list()
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
