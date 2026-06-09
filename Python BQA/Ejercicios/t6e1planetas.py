# Creamos lista con los 8 planetas
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

print("EXPLORADOR DE PLANETAS")

# Pedimos el número a la usuaria
numero = int(input("Introduce un número del 1 al 8 para elegir un planeta: "))

# Validamos si el número está dentro del rango
if 1 <= numero <= 8:
    # Restamos 1 para adaptarlo al índice de Python
    indice = numero - 1
    planeta_elegido = planetas[indice]
    print(f"El planeta número {numero} es: {planeta_elegido} ")
else:
    # Mensaje de error si mete un número inválido
    print("Error: Número inválido. Debes introducir un número entre 1 y 8.")