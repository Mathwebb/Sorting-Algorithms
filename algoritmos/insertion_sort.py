def insertion_sort(vet):
    j = 2
    cont = 0
    for i in range(1, len(vet)):
        cont += 1
        if vet[i-1] > vet[i]:
            r = i
            while vet[r-1] > vet[r]:
                cont += 1
                temp = vet[r-1]
                vet[r-1] = vet[r]
                vet[r] = temp
                r -= 1
                if r == 0:
                    break

    return vet, cont
