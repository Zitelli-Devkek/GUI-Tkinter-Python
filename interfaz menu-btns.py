import tkinter as tk 
from tkinter import filedialog as fd
from tkinter import messagebox
import webbrowser
window = tk.Tk()

def helplol():
    tk.messagebox.showinfo(message="Usted será redirigido a una nueva pagina", title="Aviso")
    webbrowser.open("https://www.psicologia-online.com/como-asumir-que-alguien-no-te-quiere-366.html")

def abrirarchivo():
    fichero = fd.askopenfilename(title="Abrir archivo")
    print(fichero) 

def guardararchivo():
    fichero2 = fd.asksaveasfilename(title="Guardar archivo")
    print (fichero2)


menubar = tk.Menu(window)

window.config(menu=menubar)

archivo = tk.Menu(menubar, tearoff=0)
editar = tk.Menu(menubar, tearoff=0)
ayuda = tk.Menu(menubar, tearoff=0)



menubar.add_cascade(label="Archivo", menu=archivo)

archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir", command=abrirarchivo)
archivo.add_command(label="Guardar", command=guardararchivo)
archivo.add_command(label="Cerrar")
archivo.add_separator()
archivo.add_command(label="Salir", command=window.quit)



menubar.add_cascade(label="Editar", menu=editar)

editar.add_command(label="Cortar")
editar.add_command(label="Copiar")
editar.add_command(label="Pegar")



menubar.add_cascade(label="Ayuda", menu=ayuda)

ayuda.add_command(label="Ayuda", command=helplol)
ayuda.add_separator()
ayuda.add_command(label="Acerca de")




window.mainloop()


