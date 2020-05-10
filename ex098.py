def contador(ini, fim, pas):
    print('=' * 47)
    import time
    if pas < 0:
        pas *= (-1)
    print(f'Contagem regressiva de {ini} até {fim} em {pas}')
    if ini < fim:
        while ini <= fim:
            time.sleep(0.3)
            print(f' {ini} ', end='')
            ini += pas
    elif ini > fim:
        while ini >= fim:
            time.sleep(0.3)
            print(f' {ini} ', end='')
            ini -= pas
    print(' FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize a Contagem!')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
contador(i, f, p)
