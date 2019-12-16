frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na sua frase.'.format(frase.count('a')))
print('Na primeira vez aparece na pos {} e na segunda {}'.format(frase.find('a')+1, frase.rfind('a')+1))
