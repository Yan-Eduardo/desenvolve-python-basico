#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
# Dica: letra in "aeiou". Exemplo:

frase = input("Digite uma frase: ")

vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiou":
        vogais += 1
        indices.append(i)

print("Vogais:", vogais)
print("Índices:", indices)