lista_ = []
maior_pos_ = []
for c_ in range(5):
    valores_ = int(input('Digite um valor: '))
    if not lista_:
        lista_.append(valores_)
        print("Adicionado ao final da lista")
    elif valores_ >= lista_[-1]:
        lista_.insert(lista_.index(lista_[-1])+1, valores_)
        print("Adicionado ao final da lista")
        #print(f"Maior valor {lista_[-1]}, e posição {lista_.index(lista_[-1])}")
    elif valores_ <= lista_[0]:
        lista_.insert(lista_.index(lista_[0]), valores_)
        print(f"Adicionado na posição {lista_.index(lista_[0])}")
    elif valores_ <= lista_[1]:
        lista_.insert(lista_.index(lista_[1]), valores_)
        print(f"Adicionado na posição {lista_.index(lista_[1])}")
    elif valores_ <= lista_[2]:
        lista_.insert(lista_.index(lista_[2]), valores_)
        print(f"Adicionado na posição {lista_.index(lista_[2])}")
    elif valores_ <= lista_[3]:
        lista_.insert(lista_.index(lista_[3]), valores_)
        print(f"Adicionado na posição {lista_.index(lista_[3])}")
    '''else:
        lista_.insert(c_, valores_)'''
print(lista_)
#Resoulução feita sem ajuda do professor