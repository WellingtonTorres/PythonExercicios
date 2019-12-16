palavras_ = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
             'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for pos in palavras_:
    print(f'\nA palavra {pos} tem as vogais: ', end=' ')
    list_ = []
    for letra_ in pos:
        if letra_.lower() in 'aeiou':
         print(letra_, end=' ')
