# Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
#Pelo menos 8 caracteres de comprimento.
#Contém pelo menos uma letra maiúscula e uma letra minúscula.
#Contém pelo menos um número.
#Contém pelo menos um caractere especial (por exemplo, @, #, $).

def validador_senha(senha):
    if len(senha) < 8:
        return False
    elif not any(caractere.isupper() for caractere in senha):
        return False
    elif not any(caractere.islower() for caractere in senha):
        return False
    elif not any(caractere.isdigit() for caractere in senha):
        return False
    elif not any(caractere in "!@#$%¨&*()_+-=/" for caractere in senha):
        return False
    else:
        return True

senha = input("digite sua senha: ")

if validador_senha(senha) == True: #decidi colocar um print invés de somente true ou falso para indicar melhor o resultado
    print("Senha forte")
else:
    print("Senha fraca")