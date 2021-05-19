#ejemplo bind
import tkinter as tk
window = tk.Tk()
def letras(evento): 
    print (evento.char)
    print (evento.x)

window.bind("<Key>", letras)


"""

"""
def saludar(saludar):
    print("Bienvenido") 

def despedir(despedir):
    print("Nos vemos") 


window.bind("<Enter>", saludar)
window.bind("<Leave>", despedir)
"""
"""
def detect (evento):
    if evento.num == 2:
        print ("ruedita") 
    elif evento.num == 1: 
        print ("izq") 
    else:
        print ("der")
 

window.bind("<Button-1>",detect )
window.bind("<Button-3>",detect )
window.bind("<Button-2>", detect )

window.mainloop()