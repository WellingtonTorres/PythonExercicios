def voto(anonacimento):
    from datetime import datetime
    '''
    :param anonacimento: Informar ano de nascimento para saber sobre o seu direito ao voto
    :return: Não há return
    @WellingtonTorres
    '''
    idade = datetime.now().year - anonacimento
    if idade < 14:
        return f'Com {idade} anos: NÃO VOTA.'
    elif (14 <= idade <= 17) or (idade > 65):
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# MAIN
anonasc = int(input('Em qual ano você nasceu? '))
print(voto(anonasc))
