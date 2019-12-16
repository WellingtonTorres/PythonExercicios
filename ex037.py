nInt = int(input('Digite um numero inteiro: '))
print('Deseja converter o numero \033[7;36m{}\033[m em quais das opções abaixo: \n Digite:'.format(nInt))
conv = str(input(' 1 para Binário \n 2 para Octal \n 3 para Hexadecimal \n --->'))

if conv == '1':
    convResult = bin(nInt)
elif conv == '2':
    convResult = oct(nInt)
elif conv == '3':
    convResult = hex(nInt)
else:
     print('Não existe o numero {} para conversão!'.format(conv))
print(convResult[2:])
