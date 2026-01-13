asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
reprobadadas = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "? "))
    if nota < 5:
        reprobadadas.append(asignatura)
print("Tienes que repetir: " + str(reprobadadas))