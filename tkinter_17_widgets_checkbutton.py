import tkinter as tk

def mostrar_seleccion():
    seleccionados = []
    if var1.get():
        seleccionados.append("Opción 1")
    if var2.get():
        seleccionados.append("Opción 2")
    if var3.get():
        seleccionados.append("Opción 3")
    
    print("Seleccionados:", seleccionados)

root = tk.Tk()

# Variables asociadas a cada Checkbutton
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Checkbuttons
check1 = tk.Checkbutton(root, text="Opción 1", variable=var1, width=20, height=2)
check2 = tk.Checkbutton(root, text="Opción 2", variable=var2, width=20, height=2)
check3 = tk.Checkbutton(root, text="Opción 3", variable=var3, width=20, height=2)

check1.pack()
check2.pack()
check3.pack()

# Botón para mostrar las opciones seleccionadas
boton_mostrar = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.pack()

root.mainloop()
