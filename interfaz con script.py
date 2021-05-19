import tkinter as tk 
window = tk.Tk() 

"""
#ejemplo bind
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

"""
leche = tk.IntVar()
azucar = tk.IntVar()

def pedido ():
    cadena = "Cafe "
    if leche.get():
         cadena += ("con leche")
    else:
        cadena += ("sin leche ") 
    
    if azucar.get():
        cadena += (" y con azucar")
    else:
        cadena +=(" y sin azucar")
    print (cadena)



chkbutton1 = tk.Checkbutton(window, text="con leche", variable=leche, onvalue=1, offvalue=0, command=pedido)
chkbutton2 = tk.Checkbutton(window, text="con azucar", variable=azucar, onvalue=1, offvalue=0, command=pedido)

chkbutton1.pack()
chkbutton2.pack()

window.mainloop()