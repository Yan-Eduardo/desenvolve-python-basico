#Escreva um script que dado uma frase conta os espaços em branco.

def contaEspacos(frase):
    espacos = 0
    for i in range(len(frase)):
        if frase[i] == " ":
            espacos += 1
    return espacos

frase = input("Digite a frase: ")

print("Espaços em branco:", (contaEspacos(frase)))