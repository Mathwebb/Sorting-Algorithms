import time
import random

import executa_algoritmos
from algoritmos.bubble_sort import bubble_sort
from algoritmos.insertion_sort import insertion_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.quick_sort import quickSort

tam_vet = 500
print("Execuções para lista aleatoria:")
list_aleat = executa_algoritmos.executa_lista_aleatoria(tam_vet, 0, 999)
print(list_aleat)
list_aleat = executa_algoritmos.executa_lista_aleatoria(tam_vet, 0, 999)
print(list_aleat)
list_aleat = executa_algoritmos.executa_lista_aleatoria(tam_vet, 0, 999)
print(list_aleat, "\n")

print("Execuções para lista ordenada:")
list_ord = executa_algoritmos.executa_lista_ordenada(tam_vet)
print(list_ord)
list_ord = executa_algoritmos.executa_lista_ordenada(tam_vet)
print(list_ord)
list_ord = executa_algoritmos.executa_lista_ordenada(tam_vet)
print(list_ord, "\n")

print("Execuções para lista inversamente ordenada:")
list_ord_inv = executa_algoritmos.executa_lista_ordenada_inv(tam_vet)
print(list_ord_inv)
list_ord_inv = executa_algoritmos.executa_lista_ordenada_inv(tam_vet)
print(list_ord_inv)
list_ord_inv = executa_algoritmos.executa_lista_ordenada_inv(tam_vet)
print(list_ord_inv, "\n")
