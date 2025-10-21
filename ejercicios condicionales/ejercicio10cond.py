pregunta = input('quieres pizza vegetariana:(si/no)')
ingreBasi = 'mozarella, tomate '
if pregunta == 'si':
    vegetarian = input('elige ingredientes: (Pimiento, tofu)')
    print('has elegido vegetariana con: ' + ingreBasi + vegetarian)
else:
    no = input('elige ingredientes: (Pepperoni, jamon, salmon)')
    print('has elegido no vegetariana con: ' + ingreBasi + no)