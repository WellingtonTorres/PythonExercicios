def voto(anonacimento):
    from datetime import datetime
    '''
    :param anonacimento: Informar ano de nascimento para saber sobre o seu direito ao voto
    :return: Não há return
    @WellingtonTorres
    '''
    idade = datetime.now().year - anonacimento
    print(f'Com {idade} anos:', end=' ')
    if idade < 14:
        print('NEGADO.')
    elif (14 <= idade <= 17) or (idade > 65):
        print('VOTO OPCIONAL.')
    elif 18 <= idade <= 65:
        print('VOTO OBRIGATÓRIO.')


# MAIN
anonasc = int(input('Em qual ano você nasceu? '))
voto(anonasc)
