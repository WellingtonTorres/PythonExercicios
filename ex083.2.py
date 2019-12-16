cont_esq_ = cont_dir_ = 0
expressao_ = str(input('Digite a expressão: '))
for simb in expressao_:
    if simb == '(':
        cont_esq_ += 1
    elif simb == ')':
        cont_dir_ += 1
if cont_esq_ == cont_dir_:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
