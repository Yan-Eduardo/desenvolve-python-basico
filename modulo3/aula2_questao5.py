genero = input("digite o genero(M/F): ")
idade = int(input("digite a sua idade: "))
tservico = int(input("digite o tempo de servico: "))

print ((genero=="M" and (idade>65) or (tservico>=30)) or (genero=="F" and (idade>60) and (tservico>=25)))