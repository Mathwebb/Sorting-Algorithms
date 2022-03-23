import random
import time


def quickSort(A, p, u):
    i = p
    j = u
    x = A[int((p + u) / 2)]
    while i <= j:
        while A[i] < x:
            i = i + 1;
        while A[j] > x:
            j = j - 1;
        if i <= j:
            troca(A, i, j)
            i = i + 1;
            j = j - 1;

    if (p < j):
        quickSort(A, p, j);
    if (u > i):
        quickSort(A, i, u);


def troca(lista, x, y):
    aux = lista[x]
    lista.insert(x, lista[y])
    del (lista[x + 1])
    lista.insert(y, aux)
    del (lista[y + 1])


x = 100

start = time.perf_counter()
listaC = []
for i in range(x):
    listaC.append(i)
# print(listaC)
pivo = len(listaC) - 1
quickSort(listaC, 0, pivo)
# print("Lista ordenada: ", listaC)
end = time.perf_counter()
print("Tempo na lista crescente: ", end - start)

start = time.perf_counter()
listaA = []
for i in range(x):
    listaA.append(random.randrange(1, x))
# print(listaA)
pivo = len(listaA) - 1
quickSort(listaA, 0, pivo)
# print("Lista ordenada: ", listaA)
end = time.perf_counter()
print("Tempo na lista aleatória: ", end - start)

start = time.perf_counter()
listaD = []
for i in range(x):
    listaD.append(x - i - 1)
# print(listaD)
pivo = len(listaD) - 1
quickSort(listaD, 0, pivo)
# print("Lista ordenada: ", listaD)
end = time.perf_counter()
print("Tempo na lista decrescente: ", end - start)