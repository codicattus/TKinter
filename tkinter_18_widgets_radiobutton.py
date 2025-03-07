import tkinter as tk

def mostrar_seleccion():
    seleccion = var.get()
    print("Opción seleccionada:", seleccion)

root = tk.Tk()

# Variable asociada a los Radiobuttons
var = tk.StringVar()

# Radiobuttons
rb1 = tk.Radiobutton(root, text="Opción A", variable=var, value="A")
rb2 = tk.Radiobutton(root, text="Opción B", variable=var, value="B")
rb3 = tk.Radiobutton(root, text="Opción C", variable=var, value="C")

rb1.pack()
rb2.pack()
rb3.pack()

# Botón para mostrar la opción seleccionada
boton_mostrar = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.pack()

root.mainloop()
