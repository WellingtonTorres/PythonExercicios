import random
import time
jogo_ = [0, 0, 0, 0, 0, 0]
print('-' * 25)
print("JOGUE NA MEGA SENA")
print('-' * 25)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {n} JOGOS!')
for c in range(n):
    time.sleep(1)
    for p in range(0, 6):
        while True:
            verify = random.randint(1, 60)
            if verify in jogo_:
                verify = random.randint(1, 60)
            else:
                break
        jogo_[p] = verify
    jogo_.sort()
    print(f'Jogo {c+1:^2}: {jogo_}')
