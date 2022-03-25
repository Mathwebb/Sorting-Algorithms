def insertion_sort(vet):
    j = 2
    for i in range(1, len(vet)):
        if vet[i-1] > vet[i]:
            r = i
            while vet[r-1] > vet[r]:
                temp = vet[r-1]
                vet[r-1] = vet[r]
                vet[r] = temp
                r -= 1
                if r == 0:
                    break

    return vet
