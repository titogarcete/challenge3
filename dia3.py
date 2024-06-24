# Solicitar al usuario que ingrese una cadena
cadena = input("Introduce una cadena para contar sus vocales: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Contar las vocales
contador_vocales = 0

for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1

# Mostrar el resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")
