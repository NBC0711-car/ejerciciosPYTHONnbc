palabra = input("Introduce una palabra: ")
letras = list(palabra)

es_palindromo = True
n = len(letras)

for i in range(n // 2):
    primera = letras[i]
    ultima = letras[n - 1 - i]
    
    if primera != ultima:
        es_palindromo = False
        break

if es_palindromo:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")