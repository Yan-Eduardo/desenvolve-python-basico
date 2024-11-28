import emoji

print("Emojis Disponíveis:")
print(emoji.emojize(":red_heart:"), "-", ":red_heart:")
print(emoji.emojize(":thumbs_up:"), "-", ":thumbs_up:")
print(emoji.emojize(":thumbs_down:"), "-", ":thumbs_down:")
print(emoji.emojize(":sad_but_relieved_face:"), "-", ":sad_but_relieved_face:")

frase = input("Digite uma frase e ela será emojizada: ")

print("Frase emojizada:")
print(emoji.emojize(frase))