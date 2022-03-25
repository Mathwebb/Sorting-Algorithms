import time
import random

from algoritmos.bubble_sort import bubble_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.quick_sort import quickSort


def gera_vetor_aleatorio(tam, lim_inf, lim_sup):
    vetor = []
    for i in range(tam):
        aleatorio = random.randrange(lim_inf, lim_sup)
        vetor.append(aleatorio)
    return vetor


def gera_vetor_ordenado(tam):
    vetor = []
    for i in range(tam):
        vetor.append(i)
    return vetor


def gera_vetor_ordenado_inv(tam):
    vetor = []
    for i in range(tam-1, -1, -1):
        vetor.append(i)
    return vetor


def executa_lista_aleatoria(tam, lim_inf, lim_sup):
    vet = gera_vetor_aleatorio(tam, lim_inf, lim_sup)
    vet_ord = vet
    tempos = {}

    # bubble sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    bubble_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Bubble"] = (tempo_final-tempo_inicial)

    # insertion sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    insertion_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Insertion"] = (tempo_final-tempo_inicial)

    # heap sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    heap_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Heap"] = (tempo_final-tempo_inicial)

    # merge sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    vet_ord = merge_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Merge"] = (tempo_final-tempo_inicial)

    # quick sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    quickSort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Quick"] = (tempo_final-tempo_inicial)

    return tempos


def executa_lista_ordenada(tam):
    vet = gera_vetor_ordenado(tam)
    vet_ord = vet
    tempos = {}

    # bubble sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    bubble_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Bubble"] = (tempo_final-tempo_inicial)

    # insertion sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    insertion_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Insertion"] = (tempo_final-tempo_inicial)

    # heap sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    heap_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Heap"] = (tempo_final-tempo_inicial)

    # merge sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    vet_ord = merge_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Merge"] = (tempo_final-tempo_inicial)

    # quick sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    quickSort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Quick"] = (tempo_final-tempo_inicial)

    return tempos


def executa_lista_ordenada_inv(tam):
    vet = gera_vetor_ordenado_inv(tam)
    vet_ord = vet
    tempos = {}

    # bubble sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    bubble_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Bubble"] = (tempo_final-tempo_inicial)

    # insertion sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    insertion_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Insertion"] = (tempo_final-tempo_inicial)

    # heap sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    heap_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Heap"] = (tempo_final-tempo_inicial)

    # merge sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    vet_ord = merge_sort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Merge"] = (tempo_final-tempo_inicial)

    # quick sort
    vet_ord = vet.copy()
    tempo_inicial = time.perf_counter()
    quickSort(vet_ord)
    tempo_final = time.perf_counter()
    tempos["Quick"] = (tempo_final-tempo_inicial)

    return tempos
