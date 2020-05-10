def sPrint(msg):
    length = len(msg) + 2
    print('*' * length)
    print(f'{msg:^{length}}')
    print('*' * length)


# Main
txt = str(input('Texto: '))
sPrint(txt)
