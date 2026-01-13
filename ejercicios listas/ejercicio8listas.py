palabra = input("Introduce una palabra: ")
palabra_reves = palabra[::-1]
if palabra == palabra_reves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")