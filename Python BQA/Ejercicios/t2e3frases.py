# Pedimos una frase a la usuaria
frase = input("Introduce una frase: ")

# Usamos las herramientas de Python para manipular el texto
longitud = len(frase)
mayusculas = frase.upper()
minusculas = frase.lower()

# Mostramos los resultados
print("La longitud de la frase es:", longitud, "caracteres")
print("La frase en mayúsculas:", mayusculas)
print("La frase en minúsculas:", minusculas)