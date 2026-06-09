# Creamos lista con los 12 meses del año
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

print("EL CALENDARIO")

# Pedimos el número del mes
numero_mes = int(input("Introduce un número del 1 al 12: "))

# Validamos que el número sea correcto
if 1 <= numero_mes <= 12:
    # Adaptamos al índice de Python
    indice = numero_mes - 1
    mes_elegido = meses[indice]
    
    print(f"El mes correspondiente es: {mes_elegido}")
    
    # Condición especial: Si el mes es Junio, mostramos el mensaje extra
    if mes_elegido == "Junio":
        print("¡EL MEJOR MES!")
else:
    print("Error: Por favor, introduce un número válido entre 1 y 12.")