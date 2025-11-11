frase = input("Introduce una frase: ")
letra = input("Introduce una letra para buscar: ")
conteo = 0  
for caracter in frase:  
    if caracter == letra:  
        conteo = conteo + 1  

print(f"La letra '{letra}' aparece {conteo} veces en la frase.")