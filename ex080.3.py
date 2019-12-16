lista_ = []
for c_ in range(5):
    valores_ = int(input('Digite um valor: '))
    if not lista_ or valores_ >= lista_[-1]:
        lista_.append(valores_)
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista_):
            if valores_ <= lista_[pos]:
                lista_.insert(pos, valores_)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print(lista_)
#Resoulução Professor