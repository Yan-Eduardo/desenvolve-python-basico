n = int(input("digite um valor: "))
maior = 0

while n > 0:
    x = int(input("digite um valor: "))

    if x > maior:
        maior = x
    n -= 1

print(maior)