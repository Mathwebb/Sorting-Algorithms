# Heap Sort
def filho_esquerda(indice):
    indice += 1
    return indice*2-1


def filho_direita(indice):
    indice += 1
    return indice*2


def constroi_heap_max(vetor):
    for i in range(len(vetor)//2 - 1, -1, -1):
        maior = i
        pai = vetor[i]
        if (i + 1) * 2 - 1 < len(vetor):
            if vetor[filho_esquerda(i)] > vetor[maior]:
                maior = filho_esquerda(i)
        if (i+1) * 2 < len(vetor):
            if vetor[filho_direita(i)] > vetor[maior]:
                maior = filho_direita(i)
        if maior != i:
            temp = vetor[i]
            vetor[i] = vetor[maior]
            vetor[maior] = temp
            vetor = refaz_heap_max(vetor, maior)
    return vetor


def refaz_heap_max(vetor, i):
    if i > len(vetor)//2 - 1:
        return vetor

    maior = i
    pai = vetor[i]
    if (i + 1) * 2 - 1 < len(vetor):
        if vetor[filho_esquerda(i)] > vetor[maior]:
            maior = filho_esquerda(i)
    if (i + 1) * 2 < len(vetor):
        if vetor[filho_direita(i)] > vetor[maior]:
            maior = filho_direita(i)
    if maior != i:
        temp = vetor[i]
        vetor[i] = vetor[maior]
        vetor[maior] = temp
        vetor = refaz_heap_max(vetor, maior)
        if i == 0 and vetor[i] < vetor[i+1]:
            temp = vetor[i]
            vetor[i] = vetor[maior]
            vetor[maior] = temp
    return vetor


def heap_sort(vetor):
    heap_max = constroi_heap_max(vetor)[0:]
    for i in range(len(vetor)-1, -1, -1):
        heap_max[0], heap_max[i] = heap_max[i], heap_max[0]
        vetor[i] = heap_max[i]
        heap_max.remove(heap_max[i])
        heap_max = refaz_heap_max(heap_max, 0)
    return vetor
