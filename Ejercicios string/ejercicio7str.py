correo = input('Introduzca su correo electronico: ')
partesCorreo = correo.split('@')
correoMod = partesCorreo[0]
nuevoCorreo = (correoMod + '@ce.es')
print(nuevoCorreo)