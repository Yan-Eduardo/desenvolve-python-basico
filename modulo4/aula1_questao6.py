experimentos = int(input("digite o numero de experimentos realizados: "))
count = 0
coelhos, ratos, sapos = 0, 0, 0

while count < experimentos:
    quant = int(input("digite a quantidade de cobaias: "))
    tipo = input("digite o tipo de cobaia(C/R/S): ")

    if tipo == "C":
        coelhos += quant
    elif tipo == "R":
        ratos += quant
    else:
        sapos += quant
    count += 1

total = coelhos + ratos + sapos
porcent_coelhos = (coelhos / total) * 100
porcent_ratos = (ratos / total) * 100
porcent_sapos = (sapos / total) * 100

print(f"Total de cobaias {total}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos {sapos}")
print(f"Percentual de coelhos: {porcent_coelhos:.2f} %")
print(f"Percentual de ratos: {porcent_ratos:.2f} %")
print(f"Percentual de sapos: {porcent_sapos:.2f} %")