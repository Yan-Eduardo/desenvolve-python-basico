#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores.
#Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista,
#adicionando ao final os elementos remanescentes da maior lista.
#Exemplo de interação via terminal (entradas em negrito):
#Digite a quantidade de elementos da lista 1: 4
#Digite os 4 elementos da lista 1:
#1
#2
#3
#4
#Digite a quantidade de elementos da lista 2: 6
#Digite os 6 elementos da lista 2:
#5
#6
#7
#8
#9
#10
#Lista intercalada: 1 5 2 6 3 7 4 8 9 10

lista1 = []
lista2 = []
intercalada = []
maior = 0

#entrada
lista1_elementos = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {lista1_elementos} elementos da lista 1:")
for i in range(lista1_elementos):
    lista1.append(int(input()))

lista2_elementos = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {lista2_elementos} elementos da lista 2:")
for i in range(lista2_elementos):
    lista2.append(int(input()))

if lista1_elementos > lista2_elementos:
    maior = 1
else:
    maior = 2

if maior == 1:
    for i in range(len(lista2)):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    for i in range(lista1_elementos - lista2_elementos):
        count = lista1_elementos - lista2_elementos
        intercalada.append(lista1[-count])
        count -= 1
else:
    for i in range(len(lista1)):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    for i in range(lista2_elementos - lista1_elementos):
        count = lista2_elementos - lista1_elementos
        intercalada.append(lista2[-count])
        count -= 1
print("Lista intercalada:", intercalada)