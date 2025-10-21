nomPro = input('Nombre del producto: ')
precPro = float(input('Precio del producto: '))
numPro = int(input('y numero de unidades: '))

costeTot = precPro * numPro

print (f'Nombre: {nomPro} Precio: {precPro:06.2f} unidades: {numPro:3d} coste total: {costeTot:08.02f}')