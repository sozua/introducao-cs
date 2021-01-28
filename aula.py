def cloneArray(array):
    clone = []
    for item in array:
        clone.append(item)
    return clone


def cloneArrayAlt(array):
    return array[:]


def clonandoArrays():
    firstOriginalArray = ['Vermelho', "Azul", "Rosa"]
    secondOriginalArray = ['Vermelho', "Azul", "Rosa"]
    firstCloneArray = cloneArray(firstOriginalArray)
    secondCloneArray = cloneArrayAlt(firstOriginalArray)

    firstCloneArray[0] = "Verde"
    secondCloneArray[0] = "Verde"

    print("Originais: \n")
    print(firstOriginalArray)
    print(secondOriginalArray)
    print("\n Clones: \n")
    print(firstCloneArray)
    print(secondCloneArray)
    print()


def pertinenciaArray():
    if "Vermelho" in ["Vermelho", "Azul"]:
        print("Vermelho está na lista")
    else:
        print("Vermelho não está na lista")


def concatenacaoArray():
    firstArray = [1, 2]
    secondArray = [3, 4]

    finalArray = firstArray + secondArray
    print(finalArray)


def repeticaoArray():
    a = [1, 2, 3]
    aTriplicado = a * 3
    print(aTriplicado)


def removendoItensArray():
    lista = [1, 2, 3, 4, 5]
    print("Antes: ", lista)
    del lista[0:3]
    print("Depois: ", lista)
