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


def multiplicar_matrizes(a, b):
    num_linhas_a, num_colunas_a, = len(a), len(a[0])
    num_linhas_b, num_colunas_b, = len(b), len(b[0])
    assert num_colunas_a == num_linhas_b

    c = []
    for linha in range(num_linhas_a):
        c.append([])
        for coluna in range(num_colunas_b):
            c[linha].append(0)
            for k in range(num_colunas_a):
                c[linha][coluna] += a[linha][k] * b[k][coluna]
    return c


arrayA = [[1, 2, 3], [4, 5, 6]]
arrayB = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arrayC = multiplicar_matrizes(arrayA, arrayB)
print(arrayC)
