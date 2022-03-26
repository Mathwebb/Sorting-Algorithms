import executa_algoritmos
from tkinter import *
from tkinter import ttk

tam_vet = 500

arq_nome = "resultados.txt"
arq = open(arq_nome, "w")
arq.write("")
arq.close()
arq = open(arq_nome, "a")

"""
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
"""

arq.close()


def mostra():
    algoritmos=[bubbl_st.get(),inser_st.get(),heap_st.get(),merge_st.get(),quick_st.get()]
    ordem=[vetor_aleat.get(),vetor_orden.get(),vetor_inver.get()]
    tam=tamanho.get()
    resultado_final = executa_algoritmos.executa_algortimos(algoritmos, ordem, tam)
    print(resultado_final)
    for (algo,orde,taman,tempo) in resultado_final:
        tv.insert("","end", values=(algo,orde,taman,tempo))


janela = Tk()
janela.title("Algoritmos de Ordenação")
janela.geometry("600x300")

texto_algoritmos = Label(janela, text="Algoritmos")
texto_algoritmos.grid(column=0, row=1)

bubbl_st = StringVar()
inser_st = StringVar()
heap_st = StringVar()
merge_st = StringVar()
quick_st = StringVar()

checkbox_bs = Checkbutton(janela, text="Bubble Sort", variable=bubbl_st, onvalue="bubble", offvalue="")
checkbox_bs.grid(column=0, row=2, padx=5, pady=5)
checkbox_bs.deselect()
checkbox_is = Checkbutton(janela, text="Insertion Sort", variable=inser_st, onvalue="insertion", offvalue="")
checkbox_is.grid(column=1, row=2, padx=5, pady=5)
checkbox_is.deselect()
checkbox_hs = Checkbutton(janela, text="Heap Sort", variable=heap_st, onvalue="heap", offvalue="")
checkbox_hs.grid(column=2, row=2, padx=5, pady=5)
checkbox_hs.deselect()
checkbox_ms = Checkbutton(janela, text="Merge Sort", variable=merge_st, onvalue="merge", offvalue="")
checkbox_ms.grid(column=3, row=2, padx=5, pady=5)
checkbox_ms.deselect()
checkbox_qs = Checkbutton(janela, text="Quick Sort", variable=quick_st, onvalue="quick", offvalue="")
checkbox_qs.grid(column=4, row=2, padx=5, pady=5)
checkbox_qs.deselect()

texto_algoritmos = Label(janela, text="Tipos de vetor")
texto_algoritmos.grid(column=0, row=3)

vetor_aleat = BooleanVar()
vetor_orden = BooleanVar()
vetor_inver = BooleanVar()

checkbox_va = Checkbutton(janela, text="Aleatório", variable=vetor_aleat, onvalue=True, offvalue=False)
checkbox_va.grid(column=0, row=4, padx=5, pady=5)
checkbox_va.deselect()
checkbox_vo = Checkbutton(janela, text="Ordenado", variable=vetor_orden, onvalue=True, offvalue=False)
checkbox_vo.grid(column=1, row=4, padx=5, pady=5)
checkbox_vo.deselect()
checkbox_vi = Checkbutton(janela, text="Invertido", variable=vetor_inver, onvalue=True, offvalue=False)
checkbox_vi.grid(column=2, row=4, padx=5, pady=5)
checkbox_vi.deselect()

texto_tamanhos = Label(janela, text="Tamanhos do vetor")
texto_tamanhos.grid(column=0, row=5)

tamanho = IntVar()

radio_bt_100 = Radiobutton(janela, text="100", variable=tamanho, value=100)
radio_bt_100.grid(column=0, row=6)
radio_bt_500 = Radiobutton(janela, text="500", variable=tamanho, value=500)
radio_bt_500.grid(column=1, row=6)
radio_bt_1000 = Radiobutton(janela, text="1000", variable=tamanho, value=1000)
radio_bt_1000.grid(column=2, row=6)
radio_bt_5000 = Radiobutton(janela, text="5000", variable=tamanho, value=5000)
radio_bt_5000.grid(column=0, row=7)
radio_bt_30000 = Radiobutton(janela, text="30000", variable=tamanho, value=30000)
radio_bt_30000.grid(column=1, row=7)
radio_bt_50000 = Radiobutton(janela, text="50000", variable=tamanho, value=50000)
radio_bt_50000.grid(column=2, row=7)
radio_bt_100000 = Radiobutton(janela, text="100000", variable=tamanho, value=100000)
radio_bt_100000.grid(column=0, row=8)
radio_bt_150000 = Radiobutton(janela, text="150000", variable=tamanho, value=150000)
radio_bt_150000.grid(column=1, row=8)

tam_esc = tamanho

botao = Button(janela, text="Mostrar Resultado", command=mostra)
botao.grid(column=0, row=9)

listaNomes=[['Quick Sort','Decrescente','10000','0,00001'], ['Heap Sort','Crescente','10000','0,0001'],['Bubble Sort','Aleatória','100000','1000000000']]

tv = ttk.Treeview(janela, columns=('algoritmo', 'ordem', 'tamanho', 'tempo'), show='headings')
tv.column('algoritmo', minwidth=0, width=100)
tv.column('ordem', minwidth=30, width=150)
tv.column('tamanho', minwidth=30, width=100)
tv.column('tempo', minwidth=0, width=100)
tv.heading('algoritmo', text='Algoritmo')
tv.heading('ordem', text='Ordem do Vetor')
tv.heading('tamanho', text='Tamanho do Vetor')
tv.heading('tempo', text='Tempo Gasto')
tv.grid(column=0, row=10)

janela.mainloop()
