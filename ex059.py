n1_ = float(input('Primeiro valor: '))
n2_ = float(input('Segundo valor:'))
opc_ = 0
while opc_ != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    ''')
    opc_ = int(input('Qual a opção? '))

    if opc_ == 1:
        result_ = n1_ + n2_
        print('A soma entre {} e  {} é {}'.format(n1_, n2_, result_))
    elif opc_ == 2:
        result_ = n1_ * n2_
        print('A multiplicação entre {} e {} é {}.'.format(n1_, n2_, result_))
    elif opc_ == 3:
        if n1_ > n2_:
            result_ = n1_
        elif n1_ < n2_:
            result_ = n2_
        else:
            print('São iguais')
        print('o numemro {} é o maior'.format(result_))
    elif opc_ == 4:
        print('Digite novamente: ')
        n1_ = float(input('Primeiro valor: '))
        n2_ = float(input('Segundo valor:'))
    else:
        print('Opção inválidade! Tente novamente!')
