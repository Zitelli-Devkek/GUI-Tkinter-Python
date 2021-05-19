import tkinter as tk 
window = tk.Tk() 

def suma():
    num1 = entry1.get() 
    num2 = entry2.get()
    try:
     sumaFinal = int(num1) + int(num2)
     entry3.insert(0,sumaFinal)
    except:
        entry3.insert(0,"tipo de dato incorrecto") 

def eliminar():
    entry1.delete(0,100)
    entry2.delete(0,100)
    entry3.delete(0,100)


label1 = tk.Label(text="Ingrese el primer numero", foreground = "white", background="blue", width=41)
label2 = tk.Label(text="Ingrese el segundo numero", foreground = "white", background="blue", width=41)
entry1 = tk.Entry(font=("Arial,15"), width=32, bg="black", fg="white")
entry2 = tk.Entry(font=("Arial,15"), width=32, bg="black", fg="white")
entry3 = tk.Entry(font=("Arial,15"), width=32, bg="black", fg="white")
button1 = tk.Button(text="Calcular", bg="green", width=40, command=suma)
button2 = tk.Button(text="Limpiar", bg="red", width=40, command=eliminar)



label1.pack()
entry1.pack() 
label2.pack() 
entry2.pack()
button1.pack() 
entry3.pack()
button2.pack() 
window.mainloop()