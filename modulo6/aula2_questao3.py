#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista chamada interseccao 
#contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista

import random

lista1 = []
lista2 = []
interseccao = []

#Criando listas
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

#Criando lista interseccão
for i in range(20):
    if lista1[i] in lista2:
        interseccao.append(lista1[i])

#função para contar quantas vezes um elemento aparece em uma lista
def contar_ocorrencias(elemento):
    contagem = lista1.count(elemento)
    contagem += lista2.count(elemento)
    return contagem
    
#Imprimindo listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista interseccão:", sorted(interseccao))
for i in interseccao:
    print(f"A quantidade de vezes que {i} aparece nas listas é: {contar_ocorrencias(i)}")