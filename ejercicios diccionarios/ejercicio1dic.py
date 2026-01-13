divisas = {"EURO":"€", "DOLAR":"$", "YEN":"¥"}
pregunta = input("Introduce una divisa (EURO, DOLAR, YEN): ").upper()
if pregunta in divisas:
    print("El símbolo de " + pregunta + " es " + divisas[pregunta])
else:
    print("La divisa introducida no está en el diccionario")