class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if(lista[j] < lista[posicao_do_minimo]):
                    posicao_do_minimo = j

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


lista = [10, 3, 9, -2, 200, 17, -8, 32, 12]

o = Ordenador()

print("Lista desordenada:", lista)
o.selecao_direta(lista)
print("Lista ordenada:", lista)
