nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu teléfono: ")
datos_personales = {
    "nombre": nombre,
    "edad": edad,
    "dirección": direccion,
    "teléfono": telefono
}
print(datos_personales["nombre"] + " tiene " + str(datos_personales["edad"]) + " años, vive en " + datos_personales["dirección"] + " y su número de teléfono es " + datos_personales["teléfono"])
