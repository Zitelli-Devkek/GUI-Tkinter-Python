import tkinter as tk 
window = tk.Tk()
window.geometry("605x200")
window.config(bg="black")
window.title("Desafío 02 by Zitelli")

label1 = tk.Label(text="Nombre", bg="#2b3030", fg="white", width=26,font=("Arial,15"))
label2 = tk.Label(text="Apellido", bg="#2b3030", fg="white", width=26,font=("Arial,15"))
label3 = tk.Label(text="DNI", bg="#2b3030", fg="white", width=26,font=("Arial,15"))
label4 = tk.Label(text="Correo electronico", bg="#2b3030", fg="white", width=26,font=("Arial,15"))


entry1 = tk.Entry(width=20)
entry2 = tk.Entry(width=20)
entry3 = tk.Entry(width=20)
entry4 = tk.Entry(width=20)


button1 = tk.Button(text="Enviar", bg="#9098d4", fg="white", width=60, height=3,) 

label1.grid(column=0, row=0, pady=1)
label2.grid(column=0, row=1, pady=1)
label3.grid(column=0, row=2, pady=1)
label4.grid(column=0, row=3, pady=1)

entry1.grid(column=1, row=0, sticky="WE")
entry2.grid(column=1, row=1, sticky="WE")
entry3.grid(column=1, row=2, sticky="WE")
entry4.grid(column=1, row=3, sticky="WE")

button1.grid(column=1, row=4, pady=19)

window.mainloop()