deposito = float(input('Introduce la cantidad de dinero depositado: '))
iAnual = 0.04
balance_1 = deposito * (1 + iAnual)
balance_2 = balance_1 * (1 + iAnual)
balance_3 = balance_2 * (1 + iAnual)
print(f'Ahorros tras el primer año: {balance_1}€')
print(f'Ahorros tras el segundo año: {balance_2}€')
print(f'Ahorros tras el tercer año: {balance_3}€')