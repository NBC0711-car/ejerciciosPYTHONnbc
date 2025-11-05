numero = int(input('dame un numero: '))
i = 1
while i <= numero:
    for j in range (i, 0, -2):
        print(j, end=' ')
    print()
    i += 2