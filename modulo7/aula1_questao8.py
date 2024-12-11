CPF = input(str("Digite um CPF(XXX.XXX.XXX-XX):"))

def valida_cpf(cpf):
    CPF_formatado = CPF[0:3] + CPF[4:7] + CPF[8:11]
    soma = 0
    multiplicador = 10
    digito_verificador = int()
    valido_invalido = str()

    for i in CPF_formatado:
        soma += int(i) * multiplicador
        multiplicador -= 1
    
    if (soma % 11) < 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - (soma % 11)
    
    CPF_formatado += str(digito_verificador)

    soma = 0
    multiplicador = 11

    for i in CPF_formatado:
        soma += int(i) * multiplicador
        multiplicador -= 1
    
    if (soma % 11) < 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - (soma % 11)
    
    CPF_formatado += str(digito_verificador)

    if (CPF[0:3] + CPF[4:7] + CPF[8:11] + CPF[12:14]) == (CPF_formatado):
        valido_invalido = ("CPF Válido")
    else:
        valido_invalido = ("CPF Inválido")

    return valido_invalido

if  len(CPF) == 14 and CPF[3] == "." and CPF[7] == "." and CPF[11] == "-":
    print(valida_cpf(CPF))
else:
    print("Formato inválido")