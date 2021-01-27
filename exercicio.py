def calcFatorial(n):
    i = 1
    total = 1
    while i <= n:
        total = total * i
        i = i + 1
    return total


def main():
    sequencia = input(
        "Digite uma sequência de números para ser calculado os seus fatoriais: ")
    numbersSplit = sequencia.split()
    i = 0
    while i < len(numbersSplit):
        numero = int(numbersSplit[i])
        print("Fatorial de", numero, "é", calcFatorial(numero))
        i = i + 1


main()
