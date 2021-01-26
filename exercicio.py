valorInicial = int(input("Digite o número a ter seus dígitos somados: "))
valorAtual = valorInicial
somaFinal = 0

while valorAtual != -1:
    if valorAtual <= 9:
        somaFinal = somaFinal + valorAtual
        valorAtual = -1
    else:
        somaFinal = somaFinal + (valorAtual % 10)
        valorAtual = valorAtual // 10
print("O resultado final dessa soma é:", somaFinal)