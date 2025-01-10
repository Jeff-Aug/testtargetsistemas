# Entrada da string
string = input("Digite uma string: ")

# Inverte a string manualmente
inverted_string = ""
for char in string:
    inverted_string = char + inverted_string

# Exibe o resultado
print(f"String invertida: {inverted_string}")
