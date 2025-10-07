numTel = input('Introduzca su numero de telefono: (tiene el siguiente formato: +ZZ-XXXXXXXXX-YY)')
partesTel = numTel.split("-")
print(partesTel)
simpTel = partesTel[1]
print(simpTel)