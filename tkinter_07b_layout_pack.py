import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label1.pack(side="top", fill="y", expand=True)

label2 = tk.Label(root, text="Etiqueta 2", bg="green")
label2.pack(side="right", fill="x", expand=True)

label3 = tk.Label(root, text="Etiqueta 3", bg="blue")
label3.pack(side="left", fill="y")

# label_center = tk.Label(root, text="Etiqueta centrada")
# label_center.pack(fill="both", expand=True)


root.mainloop()