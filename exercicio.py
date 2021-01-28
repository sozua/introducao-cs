def minMax(array):
    minima = 0
    maxima = 0
    for temperatura in array:
        if temperatura < minima:
            minima = temperatura
        if temperatura > maxima:
            maxima = temperatura

    print("A menor temperatura desse mês foi:", minima)
    print("A maior temperatura desse mês foi:", maxima)


temperaturas = [12, 32, 23, 43, -1, 2, 4]
minMax(temperaturas)
