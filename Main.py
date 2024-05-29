from tkinter import *

icon = "img/renamer.ico"
janela = Tk()
janela.title("Ranamer")
janela.iconbitmap(icon)
janela.geometry("520x200")

titulo = Label(janela, text="Ranamer")
titulo.grid(row=0, column=0, columnspan=2, sticky="ew")

janela.mainloop()