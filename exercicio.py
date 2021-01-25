import math

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = ((b ** 2)) - 4 * a * c

if delta < 0: 
    print('Não existem raízes reais para essa fórmula')
elif delta == 0:
    x = ((-b) + math.sqrt(delta)) / 2 * a
    print("A raiz dessa equação é:", x)
else:
    x1 = ((-b) + math.sqrt(delta)) / 2 * a
    x2 = ((-b) - math.sqrt(delta)) / 2 * a
    print("As raizes dessa equação é [", x1, ",", x2, "]")