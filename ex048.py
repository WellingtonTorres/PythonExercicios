r = 0
i = 0
for cont in range(1, 501, 2):
    mult_tres = cont % 3
    if mult_tres == 0:
        r += cont
        i += 1
print('A soma do intervalo é {} e acontceram {} vezes'.format(r, i))

   # print(cont, end=' ')
