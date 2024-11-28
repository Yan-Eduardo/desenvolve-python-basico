classe = input("digite o nome da classe(guerreiro/mago/arqueiro): ")
str = int(input("digite a sua força: "))
int = int(input("digite a sua inteligência: "))

print ((classe=="guerreiro" and (str>=15) and (int<=10)) or (classe=="mago" and (int>=15) and (str<=10)) or (classe=="arqueiro" and (int>5 and int<16) and (str>5 and str<16)))