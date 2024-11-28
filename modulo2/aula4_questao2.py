#solicitando a temperatura em fahrenheit
fahrenheit = int(input("digite a temperatura em Fahrenheit: "))
#convertendo para celsius
celsius = float(fahrenheit - 32) * 5 / 9

print(f'A temperatura em Celsius é: {celsius:2.0f}°')