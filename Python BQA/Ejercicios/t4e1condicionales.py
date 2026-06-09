def obtener_mensaje_color(color_elegido):
    # Pasamos el texto a minúsculas para que no falle si escriben "Rojo" o "ROJO"
    color = color_elegido.lower()
    
    if color == "rojo":
        return "Mensaje de pasión y energía."
    elif color == "verde":
        return "Mensaje de esperanza y crecimiento."
    elif color == "azul":
        return "Mensaje de calma y serenidad."
    elif color == "amarillo":
        return "Mensaje de felicidad y optimismo."
    elif color == "morado":
        return "Mensaje de sabiduría y creatividad."
    else:
        # Por si la usuaria escribe "gato" o un color que no está en la ruleta
        return "Ese color no está en la ruleta. ¡Prueba otra vez!"
    

# ENTRADA DE DATOS
print("Opciones: Rojo, Verde, Azul, Amarillo, Morado")

# Pedimos el color a la usuaria
respuesta_usuario = input("Elige un color de la lista: ")


# RESULTADO POR PANTALLA
# Llamamos a la función y guardamos el mensaje que nos devuelva
mensaje_final = obtener_mensaje_color(respuesta_usuario)

print("\n--- TU DESTINO ---")
print("Color elegido:", respuesta_usuario)
print("Resultado:", mensaje_final)