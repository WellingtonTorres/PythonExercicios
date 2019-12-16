expressao_ = []
cont_esq = cont_dir = 0
expressao_.append(str(input('Digite a expressão: ')))
for pos in expressao_:
    for verif_ in pos:
        if verif_ in '(':
            cont_esq += 1
        elif verif_ in ')':
            cont_dir += 1
if cont_dir == cont_esq:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
