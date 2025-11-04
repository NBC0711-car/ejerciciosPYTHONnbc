cantidad = float(input('cuanto vas a invertir?'))
interes = float(input('interes anual: '))
años = int(input('durante cuanto: '))

i = 1
while i <= años:  
    cantidadUse = cantidad
    capital = cantidadUse
    capital *= interes
    cantidad += capital 
    print(f'{cantidad}')
    i += 1

