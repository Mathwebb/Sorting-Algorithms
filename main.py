import executa_algoritmos
from tkinter import *

tam_vet = 500

arq_nome = "resultados.txt"
arq = open(arq_nome, "w")
arq.write("")
arq.close()
arq = open(arq_nome, "a")

print("Execuções para lista aleatoria:")
list_aleat = executa_algoritmos.executa_lista_aleatoria(tam_vet, 0, 999, arq)
print(list_aleat)
list_aleat = executa_algoritmos.executa_lista_aleatoria(tam_vet, 0, 999)
print(list_aleat)
list_aleat = executa_algoritmos.executa_lista_aleatoria(tam_vet, 0, 999)
print(list_aleat, "\n")

print("Execuções para lista ordenada:")
list_ord = executa_algoritmos.executa_lista_ordenada(tam_vet, arq)
print(list_ord)
list_ord = executa_algoritmos.executa_lista_ordenada(tam_vet)
print(list_ord)
list_ord = executa_algoritmos.executa_lista_ordenada(tam_vet)
print(list_ord, "\n")

print("Execuções para lista inversamente ordenada:")
list_ord_inv = executa_algoritmos.executa_lista_ordenada_inv(tam_vet, arq)
print(list_ord_inv)
list_ord_inv = executa_algoritmos.executa_lista_ordenada_inv(tam_vet)
print(list_ord_inv)
list_ord_inv = executa_algoritmos.executa_lista_ordenada_inv(tam_vet)
print(list_ord_inv, "\n")

arq.close()

"""
janela = Tk()
janela.title("Algoritmos de ordenação")

texto_inicial = Label(janela, text="Só testando mesmo")

janela.mainloop()
"""
