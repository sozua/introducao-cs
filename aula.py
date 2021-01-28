def criarMatriz(linhas, colunas):
    matriz = []

    for _ in range(linhas):
        linha = []
        for i in range(colunas):
            linha.append(i)
        matriz.append(linha)

    return matriz


def criarMatrizComTeclado():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    matriz = []
    for linha in range(linhas):
        linhaArray = []
        for coluna in range(colunas):
            inputValue = input('Digite o valor da coluna ' +
                               str((coluna + 1)) + ' na linha ' + str((linha + 1)) + ': ')
            linhaArray.append(inputValue)
        matriz.append(linhaArray)
    return matriz
