sexo_ = ''
while sexo_ != 'M' and sexo_ != 'F':
    sexo_ = str(input('Digite o seu sexo [M/F]: '))
    if sexo_ != 'M' and sexo_ != 'F':
        print('Dados inválidos, por gentileza insira novamente!')
print('Seu sexo é {}'.format(sexo_))
