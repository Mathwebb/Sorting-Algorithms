import time
import random

from algoritmos.bubble_sort import bubble_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.quick_sort import quickSort

vet = []
for i in range(10000):
    vet.append(random.randint(0, 99999))

vet1 = vet.copy()
vet1.sort()

vetB = vet.copy()
tempo_inicial = time.time()
bubble_sort(vetB)
# print(vetB)
tempo_final = time.time()
print("tempo bubble sort: ", tempo_final-tempo_inicial, "\n")
assert vet1, vetB

vetI = vet.copy()
tempo_inicial = time.time()
insertion_sort(vetI)
# print(vetI)
tempo_final = time.time()
print("tempo insertion sort: ", tempo_final-tempo_inicial, "\n")
assert vet1, vetI

vetH = vet.copy()
tempo_inicial = time.time()
heap_sort(vetH)
# print(vetH)
tempo_final = time.time()
print("tempo heap sort: ", tempo_final-tempo_inicial, "\n")
assert vet1, vetH

vetM = vet.copy()
tempo_inicial = time.time()
vet1 = merge_sort(vetM)
# print(vetM)
tempo_final = time.time()
print("tempo merge sort: ", tempo_final-tempo_inicial, "\n")
assert vet1, vetM

vetQ = vet.copy()
tempo_inicial = time.time()
quickSort(vet1, 0, len(vetQ)-1)
# print(vetQ)
tempo_final = time.time()
print("tempo quick sort: ", tempo_final-tempo_inicial, "\n")
assert vet1, vetQ
