
persona = {}
continuar = "si"

while continuar == "si":
    clave = input("¿Qué dato quieres introducir (ej. nombre, edad, correo)? ")
    valor = input("Introduce el valor para " + clave + ": ")
    
    persona[clave] = valor
    
    print(persona)
    
    continuar = input("¿Quieres añadir más información? (si/no): ")