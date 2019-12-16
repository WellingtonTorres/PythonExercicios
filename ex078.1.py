valores_ = i_m_ = []
maior_ = menor_ = 0


for c in range(5):
    valores_.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior_ = menor_ = valores_[c]
    else:
        if valores_[c] > maior_:
            maior_ = valores_[c]
        if valores_[c] < menor_:
            menor_ = valores_[c]
print(f'O maior valor digitado foi {maior_}, nas posições ', end=' ')
for pos, valor in enumerate(valores_):
    if valor == maior_:
        i_m_.append(pos)
for cont_ in range(len(i_m_)-1):
    print(i_m_[cont_], end=', ')
print(f'e {i_m_[len(i_m_)-1]}') #solução para não ir os pontos sem ao final
del i_m_[:]
print(f'O menor valor digitado foi {menor_}, nas posições ', end=' ')
for pos, valor in enumerate(valores_):
    if valor == menor_:
        i_m_.append(pos)
for cont_ in range(len(i_m_)-1):
    print(i_m_[cont_], end='..')
print(f'e {i_m_[len(i_m_)-1]}') #solução para não ir os pontos sem ao final
del i_m_


