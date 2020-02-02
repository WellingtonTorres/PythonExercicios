ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 28)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    stp = int(input('Mostrar nota de qual aluno? (999 Interrompe): '))
    if stp == 999:
        print('FINALIZANDO...')
        break
    if stp <= len(ficha) -1:
        print(f'Notas de {ficha[stp][0]} são {ficha[stp][1][0]} e {ficha[stp][1][1]}')
