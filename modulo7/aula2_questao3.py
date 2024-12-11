#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, 
# e considere maiúsculas e minúsculas da mesma forma

def verificaPalindromo(frase):
    frase_filtrada = [i for i in frase.lower() if ord(i) >= 97 and ord(i) <= 122]
    return frase_filtrada == frase_filtrada[::-1]

while True:
    frase = input("digite uma frase (digite 'sair' para encerrar): ")
    if frase == "sair":
        break
    if verificaPalindromo(frase):
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")