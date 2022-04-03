from algoritmos.quick_sort import quickSort
from algoritmos.insertion_sort import insertion_sort


def hibrido(vetor):
    cont = 0
    for i in range(0, len(vetor)-1):
        if vetor[i] > vetor[i+1]:
            cont += 1

    if cont <= int(0.0025*len(vetor)):
        vetor = insertion_sort(vetor)
    else:
        vetor = quickSort(vetor)
    return vetor
