def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida

# Teste
texto = input("Digite uma string: ")
print(f"String invertida: {inverter_string(texto)}")