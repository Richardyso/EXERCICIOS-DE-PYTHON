import tkinter as tk

def imprimir_mensagem():
    print("Hello World")

janela = tk.Tk()

botao_ok = tk.Button(janela, text="OK", command=imprimir_mensagem)
botao_ok.pack(side=tk.LEFT)

botao_cancelar = tk.Button(janela, text="Cancelar")
botao_cancelar.pack(side=tk.LEFT)

janela.mainloop()
