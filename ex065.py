#Maior e Menores valores
cont = total_ = media_ = ant_ = maior_ = menor_ = 0
request_ = False
while not request_:
    n_ = int(input('Digite um numero: '))
    request_ = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if request_ == 'N':
        request_ = True
    else:
        request_ = False
    cont += 1
    total_ += n_
    media_ = total_ / cont
    if cont == 1:
        maior_ = menor_ = n_
    else:
        if n_ > maior_:
            maior_ = n_
        if n_ < menor_:
            menor_ = n_
print('Você digitou {} numeros e a média foi {}'.format(cont, media_))
print('O maior numero é {} e o menor {}'.format(maior_, menor_))
