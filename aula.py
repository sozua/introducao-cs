def criarMatriz(linhas, colunas, valor):
    matriz = []

    for _ in range(linhas):
        linha = []
        for i in range(colunas):
            if valor:
                linha.append(valor)
            else:
                linha.append(i)

        matriz.append(linha)

    return matriz


def soma_matrizes(a, b):
    num_linhas = len(a)
    num_col = len(a[0])
    c = criarMatriz(num_linhas, num_col, 0)
    for lin in range(num_linhas):
        for col in range(num_col):
            c[lin][col] = a[lin][col] + b[lin][col]
    return c


print(soma_matrizes([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                    [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
