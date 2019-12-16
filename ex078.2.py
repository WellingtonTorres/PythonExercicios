#import numpy as np


class Example:

    def indices(lst, element):
        result = []
        offset = -1
        while True:
            try:
                offset = lst.index(element, offset+1)
            except ValueError:
                return result
            result.append(offset)


valores_ = []
for c in range(5):
    valores_.append(int(input(f'Digite um valor na posição {c}: ')))
maior_ = max(valores_)
print(f'O maior valor é: {maior_} nas posições {indices(valores_, maior_)}')

