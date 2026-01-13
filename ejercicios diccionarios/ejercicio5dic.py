creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for i in creditos:
    print(f"La asignatura {i} tiene {creditos[i]} créditos.")
    total += creditos[i]
print(f"El numero total de creditos es {total}")
    