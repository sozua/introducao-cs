import random
import time


class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if(lista[j] < lista[posicao_do_minimo]):
                    posicao_do_minimo = j

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolhaOtimizada(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return


def criarLista(n, quaseOrdenado):
    if quaseOrdenado:
        lista = [x for x in range(n)]
        lista[n//10] = -500
    else:
        lista = [random.randrange(1000) for x in range(n)]
    return lista


lista1 = criarLista(6000, False)
lista2 = lista1[:]
lista3 = lista1[:]

o = Ordenador()

antesBolha = time.time()
o.bolha(lista1)
depoisBolha = time.time()

print("O algoritmo de bolha antigo demorou",
      depoisBolha - antesBolha, 'segundos')

antesBolhaOtimizada = time.time()
o.bolha(lista2)
depoisBolhaOtimizada = time.time()

print("O algoritmo de bolha otimizado demorou",
      depoisBolhaOtimizada - antesBolhaOtimizada, 'segundos')

antesSelecaoDireta = time.time()
o.selecao_direta(lista3)
depoisSelecaoDireta = time.time()

print("O algoritmo de seleção direta demorou",
      depoisSelecaoDireta - antesSelecaoDireta, 'segundos')
