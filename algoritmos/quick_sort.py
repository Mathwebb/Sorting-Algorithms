def quickSort(A):
    cont = quickSort_sec(A, 0, len(A)-1, 0)
    return A, cont


def quickSort_sec(A, p, u, cont):
    i = p
    j = u
    x = A[(p + u) // 2]
    while i <= j:
        while A[i] < x:
            cont += 1
            i = i + 1
        while A[j] > x:
            cont += 1
            j = j - 1
        cont += 1
        if i <= j:
            troca(A, i, j)
            i = i + 1
            j = j - 1

    if p < j:
        cont = quickSort_sec(A, p, j, cont)
    if u > i:
        cont = quickSort_sec(A, i, u, cont)

    return cont


def troca(lista, x, y):
    aux = lista[x]
    lista[x] = lista[y]
    lista[y] = aux
