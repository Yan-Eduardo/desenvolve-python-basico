#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores),
# os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )

lista = []

while True:
    if len(lista) < 4:
        n = int(input("digite um número: "))
        lista.append(n)
    else:
        n = int(input("digite um número (digite 0 para parar): "))
        if n == 0:
            break
        else:
            lista.append(n)

print("A lista original:", lista)
print("Os 3 primeiros números:", lista[0:3])
print("Os 2 últimos números:", lista[:-3:-1])
print("A lista invertida:", lista[::-1])