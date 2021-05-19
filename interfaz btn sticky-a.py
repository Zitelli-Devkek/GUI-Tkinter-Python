import tkinter as tk 
window = tk.Tk() 
window.config(bg="black") 
window.title("Sticky")
label1 = tk.Label(text="Ingrese el primer numero", foreground = "white", background="blue", width=41)
label2 = tk.Label(text="Ingrese el segundo numero", foreground = "white", background="black", width=41)
label3 = tk.Label(text="Ingrese el segundo numero", foreground = "white", background="green", width=41)
label4 = tk.Label(text="Ingrese el segundo numero", foreground = "white", background="yellow", width=41)



window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.rowconfigure(0, weight=1) 
label1.grid(column=0,row=0, sticky="W")
label2.grid(column=1,row=0, sticky="N") 
label3.grid(column=0,row=1, sticky="S")
label4.grid(column=1,row=1, sticky="E", pady=10)





window.mainloop()