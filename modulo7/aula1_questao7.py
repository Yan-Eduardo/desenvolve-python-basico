import random

nomes = []
nome_criptografado = ""
nomes_criptografados = []
chave_aleatoria = random.randint(1, 10)

while True:
    nome = input("Nome (deixe em branco para sair): ")
    if nome == "":
        break
    nomes.append(nome)

for nome in nomes:
    for caractere in nome:
        if ord(caractere) >= 33 and ord(caractere) <= (126 - chave_aleatoria): #adicionei a formula "126 - chave" para evitar sair do intervalo de 33 a 126
            caractere = chr(ord(caractere) + chave_aleatoria)
            nome_criptografado += caractere
        else: #caso o número vá sair desse intervalo realiza um cálculo para buscar o próximo legível
            nome_criptografado += chr(ord(caractere) + chave_aleatoria - 94)
    nomes_criptografados.append(nome_criptografado)
    nome_criptografado = ""

print("Chave aleatória:", chave_aleatoria)
print("Nomes criptografados:", nomes_criptografados)