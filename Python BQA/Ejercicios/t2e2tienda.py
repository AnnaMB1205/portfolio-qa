# Precios fijos de las prendas
precio_sudadera = 20.5
precio_gorra = 5.5
precio_camiseta = 10.0

print("TIENDA DE ROPA")

# Pedimos a la usuaria la cantidad de cada artículo
cant_camisetas = int(input("¿Cuántas camisetas quieres comprar?: "))
cant_sudaderas = int(input("¿Cuántas sudaderas quieres comprar?: "))
cant_gorras = int(input("¿Cuántas gorras quieres comprar?: "))

# Total de la compra sin impuestos
total_sin_iva = (cant_camisetas * precio_camiseta) + (cant_sudaderas * precio_sudadera) + (cant_gorras * precio_gorra)

# Añadimos el 21% de IVA 
precio_final = total_sin_iva * 1.21


print("Total sin IVA: ", total_sin_iva, "euros")
print("Precio final (con 21% IVA incluido): ", precio_final, "euros")