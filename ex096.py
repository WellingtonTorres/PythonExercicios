def areaTerreno(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.2f} x {comp:.2f} é de {area:.1f}m².')


#MAIN PROGRAM
print('CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
areaTerreno(l, c)
