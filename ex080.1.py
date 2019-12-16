lista_ = []
for c_ in range(5):
    valores_ = int(input('Digite um valor: '))
    if not lista_:
        lista_.append(valores_)
        print("Adicionado ao final da lista")
    elif valores_ >= lista_[-1]:
        lista_.insert(lista_.index(lista_[-1])+1, valores_)
        print("Adicionado ao final da lista")
    elif valores_ < lista_[-1]:
        for pos, valor_ in enumerate(lista_):
            if valores_ <= lista_[pos]:
                lista_.insert(lista_.index(lista_[pos]), valores_)
                print(f'Adicionado na posição {pos} da lista!')
                break
print(lista_)
