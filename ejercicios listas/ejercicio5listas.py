numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
for i in range(len(numeros)):
    if i == len(numeros) - 1:
        print(numeros[i])
    else:
        print(str(numeros[i]), end=", ")
