#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.

nome = input("digite seu nome: ")

for i in range(len(nome)):
    print(nome[0:i+1])
