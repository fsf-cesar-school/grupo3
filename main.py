import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="CONTROL GLIC")
greeting.pack()

imagem = tk.PhotoImage(file="")
logo = tk.Label(window, image=imagem)
logo.imagem = imagem
logo.pack()

blogin = tk.Button(
    text="LOGIN",
    width=25,
    height=5,
    bg="purple",
    fg="white")
blogin.pack()

bcadastro = tk.Button(
    text="CADASTRO",
    width=25,
    height=5,
    bg="purple",
    fg="white")
bcadastro.pack()

window.mainloop()
