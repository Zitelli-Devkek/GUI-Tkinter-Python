import tkinter as tk 
window = tk.Tk() 
window.geometry("300x300") 

def saludar():
    nombre = entry1.get()
    print ("Saludos " + nombre)

entry1 = tk.Entry(font=("Arial,15"))
frame1 = tk.Frame() 
frame2 = tk.Frame()  
label1 = tk.Label(frame1, text="Etiqueta1", bg="black", fg="green") 
label2 = tk.Label(master=frame1,text="Etiqueta2", bg="black", fg="green")
label3 = tk.Label(master=frame1,text="Etiqueta3", bg="black", fg="green")
label4 = tk.Label(master= frame2, text="Etiqueta4", bg="black", fg="green")
label5 = tk.Label(frame2,text="Etiqueta5", bg="black", fg="green")
label6 = tk.Label(frame2,text="Etiqueta6", bg="black", fg="green")


#cajadetextoxd = tk.Text(bg ="blue", fg="white", font=("Arial", 20))
entry1.insert(0, "Hola mundo") 
entry1.insert(4,"Naranjaxd") 
entry1.delete(0,3)



button1 = tk.Button(text="enviar",fg="black", command=saludar)

entry1.pack() 
label1.pack() 
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
button1.pack()
#cajadetextoxd.pack()
frame1.pack()
frame2.pack() 
window.mainloop() 