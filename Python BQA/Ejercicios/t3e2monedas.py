# Convertir Euros a Dólares
def convertir_a_dolares(euros):
    dolares = euros * 1.1
    return dolares

# Convertir Euros a Libras
def convertir_a_libras(euros):
    libras = euros * 0.87
    return libras

# Pedimos una cantidad en euros
print("CONVERSOR")
cantidad_euros = float(input("Introduce la cantidad en euros (€): "))


resultado_dolares = convertir_a_dolares(cantidad_euros)
resultado_libras = convertir_a_libras(cantidad_euros)

print("\RESUMEN DE LA CONVERSIÓN")
print("Cantidad original:", cantidad_euros, "€")
print("Equivalente en Dólares:", resultado_dolares, "$")
print("Equivalente en Libras:", resultado_libras, "£")