import tkinter as tk

janela = tk.Tk()

botao_ok = tk.Button(janela, text="OK", command=lambda: print("Hello World"))
botao_ok.pack(side=tk.LEFT)

botao_cancelar = tk.Button(janela, text="Cancelar")
botao_cancelar.pack(side=tk.LEFT)

janela.mainloop()
