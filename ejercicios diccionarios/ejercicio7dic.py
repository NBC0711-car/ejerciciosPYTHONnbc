cesta = {}
continuar = "continuar"
while continuar != "salir":
    articulo = input("nombre del articulo: ")
    precio = input("precio del articulo: ")
    cesta[articulo] = precio

    continuar = input("si desea salir escriba 'salir': ")

print(cesta)