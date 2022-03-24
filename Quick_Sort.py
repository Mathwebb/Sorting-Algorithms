#Quick Sort

def quick_sort(vet):
    pivo = len(vet) - 1
    quickSort(vet, 0, pivo)

def quickSort(A, p, u):
    i = p
    j = u
    x = A[int((p + u) / 2)]
    while i <= j:
        while A[i] < x:
            i = i + 1;
        while A[j] > x:
            j = j - 1;
        if i <= j:
            troca(A, i, j)
            i = i + 1;
            j = j - 1;

    if (p < j):
        quickSort(A, p, j);
    if (u > i):
        quickSort(A, i, u);


def troca(lista, x, y):
    aux = lista[x]
    lista.insert(x, lista[y])
    del (lista[x + 1])
    lista.insert(y, aux)
    del (lista[y + 1])
