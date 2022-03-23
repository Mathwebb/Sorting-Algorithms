def insertion_sort(vet):
    for i in range(1, len(vet)):
        for t in range(1, len(vet)):
            if vet[t-1] > vet[t]:
                r = t
                while vet[r-1] > vet[r] and r-1 >= 0:
                    temp = vet[r-1]
                    vet[r-1] = vet[r]
                    vet[r] = temp
                    r -= 1
    return vet
