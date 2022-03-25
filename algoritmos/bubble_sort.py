def bubble_sort(vet):
    cont = 0
    for i in range(0, len(vet)-1):
        if vet[i] < vet[i+1]:
            cont += 1
    if cont == len(vet)-1:
        return vet

    for i in range(0, len(vet)):
        for t in range(1, len(vet)-i):
            if vet[t] < vet[t-1]:
                temp = vet[t-1]
                vet[t-1] = vet[t]
                vet[t] = temp
    return vet
