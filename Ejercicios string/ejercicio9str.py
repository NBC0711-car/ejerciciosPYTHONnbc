fechaNac = input('fecha de nacimiento formato dd/mm/aaaa: ')
fechaPartes = fechaNac.split('/')
dia = fechaPartes[0]
mes = fechaPartes[1]
año = fechaPartes[2]
print(f'dia: {dia}, mes: {mes}, año: {año}')