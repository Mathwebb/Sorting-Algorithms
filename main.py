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
tempo_inicial = time.time()
print(bubble_sort(vet1))
tempo_final = time.time()
print("tempo bubble sort: ", tempo_final-tempo_inicial, "\n")

vet1 = vet.copy()
tempo_inicial = time.time()
print(insertion_sort(vet1))
tempo_final = time.time()
print("tempo insertion sort: ", tempo_final-tempo_inicial, "\n")

vet1 = vet.copy()
tempo_inicial = time.time()
print(heap_sort(vet1))
tempo_final = time.time()
print("tempo heap sort: ", tempo_final-tempo_inicial, "\n")

vet1 = vet.copy()
tempo_inicial = time.time()
print(merge_sort(vet1))
tempo_final = time.time()
print("tempo merge sort: ", tempo_final-tempo_inicial, "\n")

vet1 = vet.copy()
tempo_inicial = time.time()
print(quickSort(vet1, 0, len(vet1)-1))
tempo_final = time.time()
print("tempo quick sort: ", tempo_final-tempo_inicial, "\n")
