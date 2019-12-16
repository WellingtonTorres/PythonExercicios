sexo_ = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]
while sexo_ not in 'MmFf':
    sexo_ = str(input('Dados inválidos, digite novamente o seu sexo: ')).upper().strip()[0]
print('O seu sexo é {}.'.format(sexo_))
