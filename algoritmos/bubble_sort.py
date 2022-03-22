def bubble_sort(vet):
    for i in range(0, len(vet)-1):
        for t in range(1, len(vet)-i):
            if vet[t] < vet[t-1]:
                temp = vet[t-1]
                vet[t-1] = vet[t]
                vet[t] = temp
    return vet
