import tkinter as tk
window = tk.Tk() 

button1 = tk.Button(text="Botón 1", bg="blue", fg="white", width=25, height=5)
button2 = tk.Button(text="Botón 2", bg="red", fg="white", width=50, height=5)
button3 = tk.Button(text="Botón 3", bg="green", fg="black", width=75, height=10)
button4 = tk.Button(text="Botón 4", bg="yellow", fg="black", width=100, height=20) 

button1.pack() 
button2.pack()
button4.pack()
button3.pack() 
window.mainloop()