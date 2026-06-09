# FUNCIÓN CON BUCLE

def calcular_nota_media():
    # 1. Preguntamos cuántas notas va a introducir
    total_notas = int(input("¿Cuántas notas deseas introducir?: "))
    
    # Creamos una caja para ir sumando las notas (empieza en 0)
    suma_total = 0
    
    # 2. El bucle dará tantas vueltas como notas haya pedido la usuaria
    for i in range(total_notas):
        # Pedimos la nota (usamos float por si tiene decimales como un 7.5)
        nota = float(input(f"Introduce la nota número {i + 1}: "))
        # Sumamos la nota a lo que ya teníamos guardado
        suma_total = suma_total + nota
        
    # 3. Calculamos la media dividiendo la suma entre el número de notas
    media = suma_total / total_notas
    return media


# EJECUCIÓN Y MUESTRA DE RESULTADOS

print("CALCULADORA DE NOTA MEDIA")

# Llamamos a la función y guardamos el resultado que nos devuelve
nota_final_media = calcular_nota_media()

print("RESULTADO")
print("La nota media final es:", nota_final_media)