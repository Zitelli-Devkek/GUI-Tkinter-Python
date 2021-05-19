import tkinter as tk 
window = tk.Tk() 
window.geometry("300x300") 

entry1 = tk.Entry(font=("Arial,15"), width=40, bg="blue", fg="white")

entry1.insert(0,"¿Cual es tu nombre? ")

entry1.pack() 
window.mainloop() 