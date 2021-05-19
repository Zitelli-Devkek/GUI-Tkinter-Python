import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser as cc
from tkinter import filedialog as fd
window = tk.Tk() 

menubar = tk.Menu(window)

window.config(menu=menubar)

fillmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=fillmenu)

#establece los botones en el menu 
fillmenu.add_command(label="Nuevo")
fillmenu.add_command(label="Guardar")
fillmenu.add_separator()
fillmenu.add_command(label="Salir", command=window.quit)



#muestra diferentes mensajes en pantalla
tk.messagebox.showinfo("A casa platita")
tk.messagebox.showwarning("Te quedaste en hierro IV")
tk.messagebox.showerror("Y te banearon la cuenta por falta de habilidad xC")

#muestra un mensaje que se puede responder con si o no
mensaje = tk.messagebox.askquestion("Salir","estas seguro de que quieres salir?")
if mensaje == "yes":
    window.destroy()

#pregunta por un color en especifico
color=cc.askcolor(title="selecciona un color")
print (color)

#da la opcion de abrir un archivo, y luego da la opcion de guardar un archivo, mostrando al final cual es el mismo
fichero = fd.askopenfilename(title="Abrir archivo")
fichero2 = fd.asksaveasfilename(title="Guardar archivo")
#print (fichero2)
print (fichero) 

window.mainloop()