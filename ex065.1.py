#Maior e Menores valores com Array
lista_n_ = []
request_ = False
while not request_:
    n_ = int(input('Digite um numero: '))
    lista_n_.append(n_)
    request_ = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if request_ == 'N':
        request_ = True
    else:
        request_ = False
    cont = len(lista_n_)
    maior_ = max(lista_n_)
    menor_ = min(lista_n_)
    media_ = sum(lista_n_) / len(lista_n_)
print('Você digitou {} numeros e a média foi {}'.format(cont, media_)) #poderia ter informado direto na impressão as variaveis
print('O maior numero é {} e o menor {}'.format(maior_, menor_))
