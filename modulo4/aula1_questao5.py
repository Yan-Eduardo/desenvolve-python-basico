n = int(input("digite o número de respondentes: "))
count = 0
soma = 0

while count < n:
    idade = int(input("digite a idade do respondente: "))
    soma += idade
    count += 1

print(f"a media das idades dos {n} respondentes é: {soma/n}")