#solicitando dados
p1 = input("Digite o nome do primeiro produto: ")
p1p = float(input("Digite o preço do primeiro produto: "))
p1q = int(input("Digite a quantidade do primeiro produto: "))
p2 = input("Digite o nome do segundo produto: ")
p2p = float(input("Digite o preço do segundo produto: "))
p2q = int(input("Digite a quantidade do segundo produto: "))
p3 = input("Digite o nome do terceiro produto: ")
p3p = float(input("Digite o preço do terceiro produto: "))
p3q = int(input("Digite a quantidade do terceiro produto: "))

#calculando o valor total
preco_total = (p1p * p1q) + (p2p * p2q) + (p3p * p3q)

#exibindo o valor total
print(f"Total: R${preco_total:,.2f}") 
