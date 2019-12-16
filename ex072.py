numext_ = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numpos_ = int(input(f'Digite um numero entre 0 e {len(numext_)-1}: '))
while numpos_ not in range(0, len(numext_)):
    numpos_ = int(input(f'Tente novamente. Digite um numero entre 0 e {len(numext_) - 1}: '))
print(f'Você digitou o número {numext_[numpos_]}.')
