import tkinter as tk
from tkinter import ttk

def mostrar_seleccion():
    seleccion = combobox.get()
    print("Opción seleccionada:", seleccion)

root = tk.Tk()

# Combobox con opciones
combobox = ttk.Combobox(root, values=["Opción A", "Opción B", "Opción C"])
combobox.pack(pady=40)

# Botón para mostrar la opción seleccionada
boton_mostrar = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.pack()

root.mainloop()
