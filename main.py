import executa_algoritmos
from tkinter import *
from tkinter import ttk

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


def mostra():
    algoritmos = [bubbl_st.get(), inser_st.get(), heap_st.get(), merge_st.get(), quick_st.get()]
    ordem = [vetor_aleat.get(), vetor_orden.get(), vetor_inver.get()]
    tam = tamanho.get()
    resultado_final = executa_algoritmos.executa_algoritmos(algoritmos, ordem, tam)
    for (algo, orde, taman, tempo) in resultado_final:
        tv.insert("", "end", values=(algo, orde, taman, tempo))


janela = Tk()
janela.title("Algoritmos de Ordenação")
janela.geometry("550x500")

texto = Label(janela, text="Bem Vindo")
texto.place(x=230, y=5)

texto_algoritmos = Label(janela, text="Algoritmos")
texto_algoritmos.place(x=20, y=20)

bubbl_st = StringVar()
inser_st = StringVar()
heap_st = StringVar()
merge_st = StringVar()
quick_st = StringVar()

checkbox_bs = Checkbutton(janela, text="Bubble Sort", variable=bubbl_st, onvalue="bubble", offvalue="")
checkbox_bs.place(x=40, y=40)
checkbox_bs.deselect()
checkbox_is = Checkbutton(janela, text="Insertion Sort", variable=inser_st, onvalue="insertion", offvalue="")
checkbox_is.place(x=140, y=40)
checkbox_is.deselect()
checkbox_hs = Checkbutton(janela, text="Heap Sort", variable=heap_st, onvalue="heap", offvalue="")
checkbox_hs.place(x=240, y=40)
checkbox_hs.deselect()
checkbox_ms = Checkbutton(janela, text="Merge Sort", variable=merge_st, onvalue="merge", offvalue="")
checkbox_ms.place(x=340, y=40)
checkbox_ms.deselect()
checkbox_qs = Checkbutton(janela, text="Quick Sort", variable=quick_st, onvalue="quick", offvalue="")
checkbox_qs.place(x=440, y=40)
checkbox_qs.deselect()

texto_algoritmos = Label(janela, text="Tipos de vetor")
texto_algoritmos.place(x=20, y=70)

vetor_aleat = BooleanVar()
vetor_orden = BooleanVar()
vetor_inver = BooleanVar()

checkbox_va = Checkbutton(janela, text="Aleatório", variable=vetor_aleat, onvalue=True, offvalue=False)
checkbox_va.place(x=40, y=90)
checkbox_va.deselect()
checkbox_vo = Checkbutton(janela, text="Ordenado", variable=vetor_orden, onvalue=True, offvalue=False)
checkbox_vo.place(x=140, y=90)
checkbox_vo.deselect()
checkbox_vi = Checkbutton(janela, text="Invertido", variable=vetor_inver, onvalue=True, offvalue=False)
checkbox_vi.place(x=240, y=90)
checkbox_vi.deselect()

texto_tamanhos = Label(janela, text="Tamanhos do vetor")
texto_tamanhos.place(x=20, y=120)

tamanho = IntVar()

radio_bt_100 = Radiobutton(janela, text="100", variable=tamanho, value=100)
radio_bt_100.place(x=140, y=140)
radio_bt_500 = Radiobutton(janela, text="500", variable=tamanho, value=500)
radio_bt_500.place(x=240, y=140)
radio_bt_1000 = Radiobutton(janela, text="1000", variable=tamanho, value=1000)
radio_bt_1000.place(x=340, y=140)
radio_bt_5000 = Radiobutton(janela, text="5000", variable=tamanho, value=5000)
radio_bt_5000.place(x=140, y=160)
radio_bt_30000 = Radiobutton(janela, text="30000", variable=tamanho, value=30000)
radio_bt_30000.place(x=240, y=160)
radio_bt_50000 = Radiobutton(janela, text="50000", variable=tamanho, value=50000)
radio_bt_50000.place(x=340, y=160)
radio_bt_100000 = Radiobutton(janela, text="100000", variable=tamanho, value=100000)
radio_bt_100000.place(x=140, y=180)
radio_bt_150000 = Radiobutton(janela, text="150000", variable=tamanho, value=150000)
radio_bt_150000.place(x=240, y=180)
radio_bt_200000 = Radiobutton(janela, text="200000", variable=tamanho, value=200000)
radio_bt_200000.place(x=340, y=180)

tam_esc = tamanho

botao = Button(janela, text="Mostrar Resultado", command=mostra)
botao.place(x=220, y=210)

tv = ttk.Treeview(janela, columns=('algoritmo', 'ordem', 'tamanho', 'tempo'), show='headings')
tv.column('algoritmo', minwidth=0, width=100)
tv.column('ordem', minwidth=30, width=100)
tv.column('tamanho', minwidth=30, width=150)
tv.column('tempo', minwidth=0, width=150)
tv.heading('algoritmo', text='Algoritmo')
tv.heading('ordem', text='Ordem do Vetor')
tv.heading('tamanho', text='Tamanho do Vetor')
tv.heading('tempo', text='Tempo Gasto')
tv.place(x=25, y=250)

calculando = Label(janela, text="")
calculando.place(x=0, y=0)

janela.mainloop()
