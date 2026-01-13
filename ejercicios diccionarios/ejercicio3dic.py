precios = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
carrito = {}
while True:
    fruta = input("Introduce la fruta que quieres comprar (o 'salir' para terminar): ").capitalize()
    if fruta.lower() == 'salir':
        break
    if fruta in precios:
        cantidad = float(input(f"¿Cuántos kilos de {fruta} quieres comprar? "))
        if fruta in carrito:
            carrito[fruta] += cantidad
        else:
            carrito[fruta] = cantidad
    else:
        print("Lo siento, esa fruta no está disponible.")

print("Carrito de la compra:")
for fruta, cantidad in carrito.items():
    print(f"{fruta}: {cantidad} kilos")
total = 0
for fruta, cantidad in carrito.items():
    total += precios[fruta] * cantidad
print(f"Total a pagar: {total:.2f} euros")

