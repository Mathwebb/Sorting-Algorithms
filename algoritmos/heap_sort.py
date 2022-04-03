# Heap Sort
def filho_esquerda(indice):
    indice += 1
    return indice*2-1


def filho_direita(indice):
    indice += 1
    return indice*2


def troca(vet, x, y):
    temp = vet[x]
    vet[x] = vet[y]
    vet[y] = temp


def constroi_heap_max(vetor):
    cont = 0
    for i in range(len(vetor)//2 - 1, -1, -1):
        cont += 3
        maior = i
        pai = vetor[i]
        if (i + 1) * 2 - 1 < len(vetor):
            cont += 1
            if vetor[filho_esquerda(i)] > vetor[maior]:
                maior = filho_esquerda(i)
        if (i+1) * 2 < len(vetor):
            cont += 1
            if vetor[filho_direita(i)] > vetor[maior]:
                maior = filho_direita(i)
        if maior != i:
            temp = vetor[i]
            vetor[i] = vetor[maior]
            vetor[maior] = temp
            vetor, cont = refaz_heap_max(vetor, maior, cont)
    return vetor, cont


def refaz_heap_max(vetor, i, cont):
    if i > len(vetor)//2 - 1:
        return vetor, cont+1

    maior = i
    pai = vetor[i]
    cont += 3
    if (i + 1) * 2 - 1 < len(vetor):
        cont += 1
        if vetor[filho_esquerda(i)] > vetor[maior]:
            maior = filho_esquerda(i)
    if (i + 1) * 2 < len(vetor):
        cont += 1
        if vetor[filho_direita(i)] > vetor[maior]:
            maior = filho_direita(i)
    if maior != i:
        troca(vetor, i, maior)
        vetor, cont = refaz_heap_max(vetor, maior, cont)
    return vetor, cont


def reconstroi_heap_max(vetor, i, f, cont):
    if i > len(vetor) // 2 - 1:
        return vetor, cont+1

    maior = i
    pai = vetor[i]
    cont += 3
    if (i + 1) * 2 - 1 < len(vetor):
        cont += 1
        if vetor[filho_esquerda(i)] > vetor[maior] and filho_esquerda(i) < f:
            maior = filho_esquerda(i)
    if (i + 1) * 2 < len(vetor):
        cont += 1
        if vetor[filho_direita(i)] > vetor[maior] and filho_direita(i) < f:
            maior = filho_direita(i)
    if maior != i:
        troca(vetor, i, maior)
        vetor, cont = reconstroi_heap_max(vetor, maior, f, cont)
    return vetor, cont


def heap_sort(vetor):
    heap_max, cont = constroi_heap_max(vetor)[0:]
    heap_fim = len(heap_max)
    for i in range(heap_fim-1, -1, -1):
        heap_max[0], heap_max[i] = heap_max[i], heap_max[0]
        vetor[i] = heap_max[i]
        heap_fim -= 1
        heap_max, cont = reconstroi_heap_max(heap_max, 0, heap_fim, cont)
    return vetor, cont
