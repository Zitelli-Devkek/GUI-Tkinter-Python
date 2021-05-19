
import tkinter as tk 
window = tk.Tk()




menubar = tk.Menu(window)

window.config(menu=menubar)

fillmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="Archivo", menu=fillmenu)
fillmenu.add_command(label="Nuevo")
fillmenu.add_command(label="Abrir")
fillmenu.add_command(label="Guardar")
fillmenu.add_command(label="Cerrar")
fillmenu.add_separator()
fillmenu.add_command(label="Salir", command=window.quit)

editar = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Editar", menu=editar)
editar.add_command(label="Cortar")
editar.add_command(label="Copiar")
editar.add_command(label="Pegar")

ayuda = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=ayuda)
ayuda.add_command(label="Ayuda")
ayuda.add_separator()
ayuda.add_command(label="Acerda de")




window.mainloop()