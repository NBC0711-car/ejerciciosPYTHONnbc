entrada = input("Introduce números separados por comas: ")
lista = entrada.split(",")
numeros = []
for n in lista:
    numeros.append(float(n))

suma = sum(numeros)
n_elementos = len(numeros)
media = suma / n_elementos

suma_varianza = 0
for n in numeros:
    suma_varianza += (n - media) ** 2
desviacion = (suma_varianza / n_elementos) ** 0.5

print("Media: " + str(media))
print("Desviación típica: " + str(desviacion))