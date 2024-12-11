#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos,
#  verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + "12345678"
    numero_formatado = numero[0:5] + "-" + numero[5:]
    print ("Número completo: ", numero_formatado)

elif len(numero) == 9:
    if numero[0] == "9":
        numero_formatado = numero[0:5] + "-" + numero[5:]
        print ("Número completo: ", numero_formatado)

    else:
        print("O primeiro dígito deve ser 9")

#Não entendi muito bem o porque verificar se o número começa em nove caso tenha 9 dígitos já que em algum ponto passará a existir telefones 
#que começam com um número diferente de 9.