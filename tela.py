from tkinter import *

janela = Tk()
janela.title("renamer")

texto_pdf1 = Label(janela, text= "Importe e passe seu argumento aqui")
texto_pdf1.grid (column= 0, row= 2)

botao_pd1 = Button(janela, text="Importe seus arquivos")
botao_pd1.grid(column=0, row= 1)

janela.mainloop()