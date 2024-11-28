idade = int(input("digite sua idade: "))
jogos = bool(input("Você já jogou pelo menos 3 jogos? (True/False): "))
jogoswin = int(input("quantos jogos ganhou: "))

print ((idade<19 and idade>15) and jogos and (jogoswin>=1))