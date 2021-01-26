def fatorial(valorInicial):
    valorTemporario = valorInicial
    valorFinal = 1
    while valorTemporario != 0:
        valorFinal = valorFinal * valorTemporario
        valorTemporario = valorTemporario - 1
    return valorFinal

def coeficienteBinomial(numerador, denominador):
    return fatorial(numerador) / (fatorial(denominador) * (fatorial(numerador - denominador)))

numerador = int(input("Digite o valor do numerador do coeficiente binomial: "))
denominador = int(input("Digite o valor do denominador do coeficiente binomial: "))

print("O valor final do coeficiente binomial é:", coeficienteBinomial(numerador, denominador))