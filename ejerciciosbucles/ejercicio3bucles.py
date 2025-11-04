numero = float(input('dame un numero: '))
i = 0
while i <= numero:
    numeros = i%2
    
    if numeros != 0:
        print(f'{i}')
    i += 1