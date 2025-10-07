cantidad = float(input('INtroduce la cantidad a invertir: '))
interes = float(input('introduce el interes anual: '))
años = int(input('Numero de años: '))
interes_decimal = interes / 100
capital_final = cantidad * (1 + interes_decimal) ** años
print=(f'El capital obtenido en la inversion es: {capital_final:.2f}')