
print("JUEGO: EL PREMIO DE LOS COLORES")
print("Tienes 5 intentos para adivinar el color premiado.\n")


for intento in range(5):
    # Pedimos el color en cada vuelta (añadimos .lower() para evitar fallos de mayúsculas)
    color = input(f"Intento {intento + 1}/5 - Introduce un color: ").lower()
    
    # Comprobamos si es el azul
    if color == "azul":
        print("¡Premio conseguido!\n")
    else:
        print("No! Prueba otro color!\n")

print("FIN DEL JUEGO")