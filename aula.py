def fatorial(n):
    if n < 1:  # base da recursão
        return 1
    return n * fatorial(n - 1)  # chamada recursiva


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(34))
