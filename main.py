import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="CONTROL GLIC")
greeting.pack()

imagem = tk.PhotoImage(file="")
logo = tk.Label(window, image=imagem)
logo.imagem = imagem
logo.pack()

login = tk.Button(
		text="LOGIN",
    width=25,
    height=5,
    bg="purple",
    fg="white")
login.pack()

cadastro = tk.Button(
    text="CADASTRO",
    width=25,
    height=5,
    bg="purple",
    fg="white")
cadastro.pack()

window.mainloop()
