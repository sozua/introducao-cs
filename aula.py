import random
import time


class Buscador:
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1


lista = [x for x in range(3000)]

antes = time.time()
posicao = Buscador().busca_binaria(lista, 2999)
depois = time.time()

print("2999 foi encontrado na posição", posicao,
      "em", depois - antes, "segundos.")
