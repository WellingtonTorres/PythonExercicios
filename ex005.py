n = int(input("Digite um número: "))
#ant = n - 1
#suc = n + 1

#print('Analisando o valor digitado {}, seu antecessor é {} e sucessor {}.'.format(n, ant, suc))

print('Analisando o valor digitado \033[1;37m{}\033[m, seu antecessor é \033[1;37;40m{}\033[m e sucessor {}.'.format(n, (n - 1), (n + 1)))

