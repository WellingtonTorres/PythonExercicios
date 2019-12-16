texto = str(input('Digite uma frase: ').upper()).split()
junto = ''.join(texto)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Palindromo!')
else:
    print('Não é palindromo!')
