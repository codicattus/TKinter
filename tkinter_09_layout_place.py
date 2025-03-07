import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label1.place(x=50, y=50)  

label2 = tk.Label(root, text="Etiqueta 2", bg="blue")
label2.place(x=150, y=150)

root.mainloop()
