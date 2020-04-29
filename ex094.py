cadastro = dict()
lista = list()
sum_idade = 0
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
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for p, v in enumerate(lista):
    sum_idade += lista[p]["idade"]
media_idade = sum_idade/len(lista)
print(f'B) A média de idade é: {media_idade} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p, v in enumerate(lista):
    if lista[p]["sexo"] in 'Ff':
        print(f'{lista[p]["nome"]}', end=', ')
print('\nD) Lista de pessoas que estão acima da média: ')
for p, v in enumerate(lista):
    if lista[p]["idade"] > media_idade:
     print(f' Nome = {lista[p]["nome"]}; sexo = {lista[p]["sexo"]}; idade = {lista[p]["idade"]}')