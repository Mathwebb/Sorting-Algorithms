import time
import random

from algoritmos.bubble_sort import bubble_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.quick_sort import quickSort


def escreve_em_arq(arq, dic, titulo):
    str_res = ""
    arq.write(titulo)
    for chave, valor in dic.items():
        str_res += chave + ": "
        str_res += str(valor) + "\n"
    str_res += "\n"
    arq.write(str_res)


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


def executa_bubble_sort(vetor):
    tempo_inicial = time.perf_counter()
    bubble_sort(vetor)
    tempo_final = time.perf_counter()
    return tempo_final - tempo_inicial


def executa_insertion_sort(vetor):
    tempo_inicial = time.perf_counter()
    insertion_sort(vetor)
    tempo_final = time.perf_counter()
    return tempo_final - tempo_inicial


def executa_heap_sort(vetor):
    tempo_inicial = time.perf_counter()
    heap_sort(vetor)
    tempo_final = time.perf_counter()
    return tempo_final - tempo_inicial


def executa_merge_sort(vetor):
    tempo_inicial = time.perf_counter()
    vetor = merge_sort(vetor)
    tempo_final = time.perf_counter()
    return tempo_final - tempo_inicial


def executa_quick_sort(vetor):
    tempo_inicial = time.perf_counter()
    quickSort(vetor)
    tempo_final = time.perf_counter()
    return tempo_final - tempo_inicial


def executa_lista_aleatoria(tam, lim_inf, lim_sup, arq=None):
    vet = gera_vetor_aleatorio(tam, lim_inf, lim_sup)
    vet_ord = vet
    tempos = {}

    # bubble sort
    vet_ord = vet.copy()
    tempos["Bubble"] = executa_bubble_sort(vet_ord)

    # insertion sort
    vet_ord = vet.copy()
    tempos["Insertion"] = executa_insertion_sort(vet_ord)

    # heap sort
    vet_ord = vet.copy()
    tempos["Heap"] = executa_heap_sort(vet_ord)

    # merge sort
    vet_ord = vet.copy()
    tempos["Merge"] = executa_merge_sort(vet_ord)

    # quick sort
    vet_ord = vet.copy()
    tempos["Quick"] = executa_quick_sort(vet_ord)

    if arq is not None:
        escreve_em_arq(arq, tempos, "Lista aleatoria\n")

    return tempos


def executa_lista_ordenada(tam, arq=None):
    vet = gera_vetor_ordenado(tam)
    vet_ord = vet
    tempos = {}

    # bubble sort
    vet_ord = vet.copy()
    tempos["Bubble"] = executa_bubble_sort(vet_ord)

    # insertion sort
    vet_ord = vet.copy()
    tempos["Insertion"] = executa_insertion_sort(vet_ord)

    # heap sort
    vet_ord = vet.copy()
    tempos["Heap"] = executa_heap_sort(vet_ord)

    # merge sort
    vet_ord = vet.copy()
    tempos["Merge"] = executa_merge_sort(vet_ord)

    # quick sort
    vet_ord = vet.copy()
    tempos["Quick"] = executa_quick_sort(vet_ord)

    if arq is not None:
        escreve_em_arq(arq, tempos, "Lista ordenada\n")

    return tempos


def executa_lista_ordenada_inv(tam, arq=None):
    vet = gera_vetor_ordenado_inv(tam)
    vet_ord = vet
    tempos = {}

    # bubble sort
    vet_ord = vet.copy()
    tempos["Bubble"] = executa_bubble_sort(vet_ord)

    # insertion sort
    vet_ord = vet.copy()
    tempos["Insertion"] = executa_insertion_sort(vet_ord)

    # heap sort
    vet_ord = vet.copy()
    tempos["Heap"] = executa_heap_sort(vet_ord)

    # merge sort
    vet_ord = vet.copy()
    tempos["Merge"] = executa_merge_sort(vet_ord)

    # quick sort
    vet_ord = vet.copy()
    tempos["Quick"] = executa_quick_sort(vet_ord)

    if arq is not None:
        escreve_em_arq(arq, tempos, "Lista inversamente ordenada\n")

    return tempos
