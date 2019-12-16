print('Gerador de PA (10 termos) ')
print('-='*8)
prim_termo_ = int(input('Primeiro Termo: '))
razao_ = int(input('Razão da PA: '))
total_termos = 10
prox_termo_ = prim_termo_
count_termos = 0
while total_termos != 0:
    count_termos += total_termos
    while total_termos > 0:
        print('{}'.format(prox_termo_), end=' ')
        print('=>' if total_termos > 1 else 'PAUSA', end=' ')
        prox_termo_ += razao_
        total_termos -= 1
    total_termos = int(input('\nQuantos termos você deseja mostrar a mais? '))
print('A progressão foi realizada com o total de {} termos'.format(count_termos))
