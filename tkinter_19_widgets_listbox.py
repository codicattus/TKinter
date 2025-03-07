import tkinter as tk

def mostrar_seleccion():
    seleccionados = listbox.curselection()
    seleccionados_texto = [listbox.get(i) for i in seleccionados]
    print("Elementos seleccionados:", seleccionados_texto)

root = tk.Tk()

# Listbox con múltiples elementos
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for item in ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]:
    listbox.insert(tk.END, item)

listbox.pack()

# Botón para mostrar los elementos seleccionados
boton_mostrar = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.pack()

root.mainloop()
