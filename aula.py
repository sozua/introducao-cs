def busca_sequencial(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False


array = [1, 2, 3, 4, 5, 6]
encontrou = busca_sequencial(array, 12)

print(encontrou)
