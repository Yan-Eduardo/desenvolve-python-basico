n1 = int(input("digite o primeiro valor: "))
n2 = int(input("digite o segundo valor: "))
n3 = int(input("digite o terceiro valor: "))

m = (n1 + n2 + n3) / 3

if m>=60:
    print("aprovado")
elif m>=40:
    print("recuperação")
else:
    print("reprovado")

print("fim")