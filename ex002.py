nome = input("Digite o seu nome: ")
print('\033[31m', "É um prazer te conhecer", nome + "!", '\033[m')
#Solucao Apresentada pelo Professor
print('\033[34m', "É um prazer te conhecer {}!".format(nome), '\033[m')