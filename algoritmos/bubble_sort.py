def bubble_sort(vet):
    cont_tam = 0

    for i in range(0, len(vet)-1):
        if vet[i] < vet[i+1]:
            cont_tam += 1
    if cont_tam == len(vet)-1:
        return vet, cont_tam

    cont = len(vet)
    for i in range(0, len(vet)):
        for t in range(1, len(vet)-i):
            cont += 1
            if vet[t] < vet[t-1]:
                cont += 1
                temp = vet[t-1]
                vet[t-1] = vet[t]
                vet[t] = temp
    return vet, cont
