edad = int(input("¿Cuál es tu edad? "))

if edad < 4:
    print("La entrada es gratis.")
elif edad <= 18:
    print("La entrada cuesta 5€.")
else:
    print("La entrada cuesta 10€.")