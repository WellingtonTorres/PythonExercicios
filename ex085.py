lista = [[], []]
n = 0
for i in range(7):
   n = int(input(f'Digite o {i+1}º valor: '))
   if n % 2 == 0:
       lista[0].append(n)
   else:
       lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(lista)
print(f'Os pares foram: {lista[0]}')
print(f'Os impares foram: {lista[1]}')
