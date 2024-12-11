#De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas,
# contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras() para ajudar a testar a 
# hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. 
# Dica: use a biblioteca random.

import random

frase = input(str("Digite uma frase: "))
def embaralhar_palavras(frase):
    frase_embaralhada = ""

    for palavra in frase.split():
        if len(palavra) >=4:
            frase_embaralhada += palavra[0]
            for letra in palavra[1:-1]:
                if letra in "çãõéóí":  #caso a letra tenha ~, ´ ou seja ç ela não é embaralhada para não se transformarem em caracteres ilegíveis
                    frase_embaralhada += letra
                else:
                    embaralhamento = random.randint(0, 10)
                    if ord(letra) >= 65 and ord(letra) <= (122 - embaralhamento): #adicionei a formula "122 - embaralhamento" para evitar sair do intervalo de 65 a 122
                        frase_embaralhada += chr(ord(letra) + embaralhamento)
                    else: #caso o número vá sair desse intervalo realiza um cálculo para buscar o próximo legível
                        frase_embaralhada += chr(abs(ord(letra) + embaralhamento - 58))
            frase_embaralhada += palavra[-1]
        else:
            frase_embaralhada += palavra
        frase_embaralhada += " "
    return frase_embaralhada

print(embaralhar_palavras(frase))