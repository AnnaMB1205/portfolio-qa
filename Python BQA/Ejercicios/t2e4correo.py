# Pedimos el correo electrónico a la usuaria
correo = input("Introduce tu dirección de correo electrónico: ")

# Manipulamos la cadena del correo electrónico
longitud_correo = len(correo)
correo_mayusculas = correo.upper()
correo_minusculas = correo.lower()

# Mostramos la información en la consola
print("La longitud del correo es:", longitud_correo, "caracteres")
print("El correo en mayúsculas:", correo_mayusculas)
print("El correo en minúsculas:", correo_minusculas)