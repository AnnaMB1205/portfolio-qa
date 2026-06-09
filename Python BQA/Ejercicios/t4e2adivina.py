
def comprobar_suerte(numero_elegido):
    # El número ganador que nos pide el ejercicio es el 4
    numero_ganador = 4
    
    # Comprobamos si el número de la usuaria es igual al ganador
    if numero_elegido == numero_ganador:
        return "¡Victoria! Has acertado el número ganador."
    else:
        return "Derrota... Ese no era el número ganador."
    

# ENTRADA DE DATOS

print("ADIVINA EL NÚMERO SECRETO")


# Pedimos el número a la usuaria 

respuesta_usuario = int(input("Elige un número entre 1 y 10: "))


# RESULTADO POR PANTALLA

mensaje_resultado = comprobar_suerte(respuesta_usuario)

print("RESULTADO")
print("Número elegido:", respuesta_usuario)
print("Mensaje:", mensaje_resultado)