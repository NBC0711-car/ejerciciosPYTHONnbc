A = [[1, 2, 3], [4, 5, 6]]
B = [[-1, 0], [0, 1], [1, 1]]
resultado = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]

for fila in resultado:
    print(fila)