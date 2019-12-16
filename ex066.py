s = i = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    i += 1
print(f'A soma dos {i} valores foi {s}')
