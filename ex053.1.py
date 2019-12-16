texto = str(input('Digite uma frase: ').upper()).split()
junto = ''.join(texto)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Palindromo!')
else:
    print('Não é palindromo!')
