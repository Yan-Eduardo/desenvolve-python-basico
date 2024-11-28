#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo 
#que possui a maior quantidade de números negativos e delete ele da lista com o operador del. 
# Você deve imprimir a lista antes e depois da deleção.
#Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
#Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random

lista = []
for i in range(20):
    lista.append(random.randint(-10, 10))

print("Original:", lista)

inicio_maior_fatia, tam_maior_fatia = 0, 0
inicio_fatia_atual, tam_fatia_atual = 0, 0

for i in range(len(lista)):
    if lista[i] < 0:
        tam_fatia_atual += 1
    else:
        if tam_fatia_atual > tam_maior_fatia:
            inicio_maior_fatia = inicio_fatia_atual
            tam_maior_fatia = tam_fatia_atual
        tam_fatia_atual = 0
        inicio_fatia_atual = i + 1

del lista[inicio_maior_fatia:inicio_maior_fatia + tam_maior_fatia]

print("Editada:", lista)
