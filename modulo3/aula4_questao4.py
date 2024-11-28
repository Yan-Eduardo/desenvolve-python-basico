distancia = float(input("digite a distância em km: "))
peso = float(input("digite o peso em kg: "))

if distancia <= 101:
    preco = 1
elif distancia > 100 and distancia <= 300:
    preco = 1.5
elif distancia > 300:
    preco = 2

if peso>10:
    taxa = 10
else:
    taxa = 0

print(f"o valor do frete é de: R${(preco*peso)+taxa:.2f}")