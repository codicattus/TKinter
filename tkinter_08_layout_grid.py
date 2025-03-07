import tkinter as tk

root = tk.Tk()

# Widget normal (1x1 celda)
label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label1.grid(row=0, column=0, sticky="nwse")

# Widget que ocupa 2 filas
label2 = tk.Label(root, text="Etiqueta 2 (rowspan=2)", bg="blue")
label2.grid(row=1, column=1, rowspan=2, sticky="nwse")

# Widget que ocupa 2 columnas
label3 = tk.Label(root, text="Etiqueta 3 (columnspan=2)", bg="green")
label3.grid(row=3, column=0, columnspan=2, sticky="nwse")

root.mainloop()



'''
Opciones más comunes de grid():

row:                  Fila en la que colocar el widget.
column:               Columna en la que colocar el widget.
sticky:               Determina en qué dirección el widget se "adherirá" al espacio disponible (norte, sur, este, oeste, o cualquier combinación).
rowspan y columnspan: Permiten que un widget ocupe varias filas o columnas.
padx y pady:          Para agregar espacio horizontal y vertical respectivamente.

'''