import random
from time import sleep
print(52*('º'))
print('Vou pensar em um número entre 0 a 5. Tente advinhar!')
print(52*('º'))
sleep(3)
n = int(input('Em que número pensei? '))
print('PROCESSANDO....')
sleep(3)
adv = random.randint(0, 5)
if n == adv:
    print('Você acertou! PARABÉNS!!!')
else:
    print('Haha como esperado... você ERROOOUU!')
print(adv)