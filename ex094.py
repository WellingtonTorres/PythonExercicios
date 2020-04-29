cadastro = dict()
lista = list()

while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: ')).strip()
    while cadastro["sexo"] not in 'MmFf':
        print('ERRO! Digite apenas M ou F!')
        cadastro['sexo'] = str(input('Sexo: ')).strip()
    cadastro['idade'] = int(input('Idade: '))
    oper = str(input('Deseja continuar? [S/N] '))
    while oper not in 'SsNn':
        print('Reponda apenas S ou N!')
        oper = str(input('Deseja continuar? [S/N] '))
    dict_copy = cadastro.copy()
    lista.append(dict_copy)
    if oper in 'Nn':
        break
print('=-=' * 25)
print(f'A) Ao todo tem(os) {len(lista)} pessoas cadastradas.')