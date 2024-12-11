#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

# tentei fazer de uma maneira diferente criando uma função que encontra todos os anagramas de uma palavra e depois verifica se ela se encontra na frase
def encontrar_anagramas(frase, palavra_obj):
    possiveis_anagramas = []
    anagramas = []
    lista_palavras = frase.lower().split()
    palavra_filtrada = "" 
    
    for i in palavra_obj: # cria uma string com os caracteres ordenados, fiz esse for pois ao usar sorted() é retornado uma lista e não uma string
        palavra_filtrada += i

    for i in range(len(palavra_filtrada)):
        possiveis_anagramas.append((palavra_filtrada[i:] + palavra_filtrada[0:(i)]))
    
    possiveis_anagramas.append(palavra_filtrada[::-1])
    
    for i in lista_palavras:
        if i in possiveis_anagramas:
            anagramas.append(i)
    
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite uma palavra objetivo: ")

if palavra_objetivo in frase.lower().split():
    print("Anagramas: ", (encontrar_anagramas(frase, sorted(palavra_objetivo))))
else:
    print("A palavra objetivo não se encontra na frase fornecida.")