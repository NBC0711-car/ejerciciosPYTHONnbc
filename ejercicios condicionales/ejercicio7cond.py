renta = int(input('Declaracion de renta: '))
if (renta < 10000):
    print('0.05 de impositivo')
if (renta < 20000 and renta > 10000):
    print('0.15 de impositivo')
if (renta < 35000 and renta > 20000):
    print('0.2 de impositivo')
if (renta < 60000 and renta > 35000):
    print('0.3 de impositivo')
if (renta > 60000):
    print('0.45 de impositivo')
