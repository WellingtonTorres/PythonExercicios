dados_alunos = list()
temp_ = list()
while True:
    temp_.append(str(input('Nome: ')))
    temp_.append(float(input('Nota 1: ')))
    temp_.append(float(input('Nota 2: ')))
    dados_alunos.append(temp_[:])
    temp_.clear()
    stp = input(str('Deseja continuar? [S/N] '))
    if stp in 'Nn':
        break
    else:
        continue
print('No  Nome  Media')
print('_' * 30)
for i, l in enumerate(dados_alunos):
    print(f'{i}   {l[0]}', end='  ')
    media_ = (l[1] + l[2]) / 2
    print(media_)
print('_' * 30)
while True:
    stp = int(input('Mostrar nota de qual aluno? (999 Interrompe): '))
    if stp == 999:
        break
    if stp <= len(dados_alunos):
        for i, l in enumerate(dados_alunos):
            if i == stp:
                print(f'A notas de {l[0]} são {l[1]} e {l[2]}')
                print('-' * 40)
