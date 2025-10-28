VALOR_BASE = 2400

puntuacion = float(input("Introduce la puntuación del empleado (ej. 0.0, 0.4, 0.6 o más): "))

nivel = ""

if puntuacion == 0.0:
    nivel = "Inaceptable"
else:
    if puntuacion == 0.4:
        nivel = "Aceptable"
    else:
        if puntuacion >= 0.6:
            nivel = "Meritorio"

cantidad_dinero = VALOR_BASE * puntuacion

print("Puntuación obtenida:", puntuacion)
print("Nivel de rendimiento:", nivel)
print("Cantidad de dinero a recibir:", cantidad_dinero, "€")