def quickSort(A):
    quickSort_sec(A, 0, len(A)-1)


def quickSort_sec(A, p, u):
    i = p
    j = u
    x = A[int((p + u) / 2)]
    while i <= j:
        while A[i] < x:
            i = i + 1
        while A[j] > x:
            j = j - 1
        if i <= j:
            troca(A, i, j)
            i = i + 1
            j = j - 1

    if p < j:
        quickSort_sec(A, p, j)
    if u > i:
        quickSort_sec(A, i, u)


def troca(lista, x, y):
    aux = lista[x]
    lista[x] = lista[y]
    lista[y] = aux
