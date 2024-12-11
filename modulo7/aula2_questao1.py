#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 

data = input("digite sua data de nascimento (dd/mm/aaaa): ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

print("Você nasceu em ", dia, " de " + meses[int(mes) - 1] + " de " + ano)