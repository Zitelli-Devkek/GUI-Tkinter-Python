import tkinter as tk 
window = tk.Tk() 
#window.geometry("300x300")#


label1 = tk.Label(text="Holaxd", foreground = "green", background="black")  
label2 = tk.Label (text = "main teemo", foreground = "blue", background="black") 
label3 = tk.Label (text= "adiós", foreground = "red", background="black") 
label1.pack()
label2.pack() 
label3.pack()
button = tk.Button(text = "Don`t play me", fg="black", bg="red", width=10, height=5) 
button.pack()
window.mainloop()

