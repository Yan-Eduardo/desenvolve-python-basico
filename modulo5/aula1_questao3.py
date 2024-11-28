import random

numero = random.randint(0, 10)

while True:
    tentativa = int(input("digite um número entre 0 e 10: "))
    if tentativa == numero:
        print("Correto! O número é: ", numero)
        break
    else:
        if tentativa > numero:
            print("Muito baixo")
        else:
            print("Muito alto")