palavras_ = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
             'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for pos in palavras_:
    print(f'A palavra {pos} tem as vogais: ', end=' ')
    list_ = []
    for c in pos:
        if c in 'AEIOU':
         list_.append(c)
    print(list_)
