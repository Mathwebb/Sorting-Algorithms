from Bubble_Sort import *
from Heap_Sort import *
from Insertion_Sort import *
from Merge_Sort import *
from Quick_Sort import *
import random
import time

tamanho = int(input('Digite o tamanho do vetor de números: '))

listaC = []
listaA = []
listaD = []

inicioC,inicioA,inicioD=0,0,0
fimC,fimA,fimD=0,0,0

for i in range(tamanho):
    listaC.append(i)
for i in range(tamanho):
    listaA.append(random.randrange(1, tamanho))
for i in range(tamanho):
    listaD.append(tamanho - i - 1)
    
print('1 - Bubble Sort')
print('2 - Heap Sort')
print('3 - Insertion Sort')
print('4 - Merge Sort')
print('5 - Quick Sort')
escolha=int(input('Escolha um algoritmo para ser testado:'))


if(escolha==1):
    inicioC = time.perf_counter()
    bubble_sort(listaC)
    fimC = time.perf_counter()
    
    inicioA = time.perf_counter()
    bubble_sort(listaA)
    fimA = time.perf_counter()
    
    inicioD = time.perf_counter()
    bubble_sort(listaD)
    fimD = time.perf_counter()
    
elif(escolha==2):
    inicioC = time.perf_counter()
    heap_sort(listaC)
    fimC = time.perf_counter()
    
    inicioA = time.perf_counter()
    heap_sort(listaA)
    fimA = time.perf_counter()
    
    inicioD = time.perf_counter()
    heap_sort(listaD)
    fimD = time.perf_counter()
    
elif(escolha==3):
    inicioC = time.perf_counter()
    insertion_sort(listaC)
    fimC = time.perf_counter()
    
    inicioA = time.perf_counter()
    insertion_sort(listaA)
    fimA = time.perf_counter()
    
    inicioD = time.perf_counter()
    insertion_sort(listaD)
    fimD = time.perf_counter()
    
elif(escolha==4):
    inicioC = time.perf_counter()
    merge_sort(listaC)
    fimC = time.perf_counter()
    
    inicioA = time.perf_counter()
    merge_sort(listaA)
    fimA = time.perf_counter()
    
    inicioD = time.perf_counter()
    merge_sort(listaD)
    fimD = time.perf_counter()
    
elif(escolha==5):
    inicioC = time.perf_counter()
    quick_sort(listaC)
    fimC = time.perf_counter()
    
    inicioA = time.perf_counter()
    quick_sort(listaA)
    fimA = time.perf_counter()
    
    inicioD = time.perf_counter()
    quick_sort(listaD)
    fimD = time.perf_counter()
    
else:
    print('Opção não existente!')

print("Tempo na lista crescente: ", fimC - inicioC)
print("Tempo na lista aleatória: ", fimA - inicioA)
print("Tempo na lista decrescente: ", fimD - inicioD)
