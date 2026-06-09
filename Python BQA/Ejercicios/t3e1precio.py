print("DATOS DEL PRODUCTO")
nombre_producto = input("Nombre del producto: ")
precio_unidad = float(input("Precio por unidad: "))
cantidad_comprar = int(input("Cantidad a comprar: "))
descuento_aplicar = float(input("Descuento en porcentaje (ej. 10): "))


# Función 1
def calcular_precio_descuento(precio, cantidad, descuento_porcentaje):
    total_bruto = precio * cantidad
    descuento_dinero = total_bruto * (descuento_porcentaje / 100)
    total_con_descuento = total_bruto - descuento_dinero
    return total_con_descuento

# Función 2: Añade el 21% de IVA
def agregar_iva(importe):
    total_con_iva = importe * 1.21
    return total_con_iva


# Datos que introdujo la usuaria
precio_descontado_total = calcular_precio_descuento(precio_unidad, cantidad_comprar, descuento_aplicar)

print("\n--- RESUMEN CON DESCUENTO ---")
print("Cantidad:", cantidad_comprar)
print("Producto:", nombre_producto)
print("Descuento aplicado:", descuento_aplicar, "%")
print("Precio total con descuento (sin IVA):", precio_descontado_total, "euros")

# Precio ya descontado con el IVA
precio_final_con_iva = agregar_iva(precio_descontado_total)

print("\TOTAL FINAL")
print("Precio final con el 21% de IVA aplicado:", precio_final_con_iva, "euros")