import datetime

data_atual = datetime.datetime.now()
data_texto = data_atual.strftime("%d/%m/%Y")
data_hora = data_atual.strftime("%H:%M")

print(data_texto)
print(data_hora)