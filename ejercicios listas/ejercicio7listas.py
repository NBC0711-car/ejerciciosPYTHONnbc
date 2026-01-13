alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
resultado = []
for i in range(len(alfabeto)):
    if (i + 1) % 3 != 0:
        resultado.append(alfabeto[i])
print(resultado)