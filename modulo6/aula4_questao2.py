#Solicite uma frase do usuário e usando compreensão de listas imprima:
#A lista de vogais da frase, ordenada alfabeticamente
#A lista de consoantes da frase
#Exemplo:
#Digite uma frase: Eu gosto de programar em Python
#Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
#Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

frase = input("Digite uma frase: ")

vogais = [letra for letra in frase if letra in 'aeiou']
print("Vogais:", sorted(vogais))

consoantes = [letra for letra in frase if letra not in 'aeiou' and letra != ' ']
print("Consoantes:", sorted(consoantes))