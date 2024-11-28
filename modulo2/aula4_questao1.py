#registrando o comprimento e a largura do terreno
comprimento = float(input('digite o comprimento do terreno: '))
largura = float(input('digite a largura do terreno: '))
preco = float(input('digite o valor do m2 da região: '))

#calculando o terreno
area_m2 = comprimento * largura
preco_total = area_m2 * preco
print(f"O valor do terreno é de R${preco_total:,.2f}")