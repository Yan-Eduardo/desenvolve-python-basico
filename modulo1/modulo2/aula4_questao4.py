#solicitando o valor em reais
valor = int(input("digite o valor em reais: "))

#calculando as notas
n100 = valor // 100
valor = valor % 100 #reduzindo do valor total para o resultado final não passar do valor dado

n50 = valor // 50
valor = valor % 50

n20 = valor // 20
valor = valor % 20

n10 = valor // 10
valor = valor % 10

n5 = valor // 5
valor = valor % 5

n2 = valor // 2
valor = valor % 2

n1 = valor // 1

#exibindo o resultado
print(f"nota(s) de 100: {n100}")
print(f"nota(s) de 50: {n50}")
print(f"nota(s) de 20: {n20}")
print(f"nota(s) de 10: {n10}")
print(f"nota(s) de 5: {n5}")
print(f"nota(s) de 2: {n2}")
print(f"nota(s) de 1: {n1}")