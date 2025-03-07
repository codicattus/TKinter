import tkinter as tk

root = tk.Tk()

# pack() coloca los widgets de manera secuencial

tk.Label(root, text="Etiqueta Pack 1").pack() 
tk.Label(root, text="Etiqueta Pack 2").pack()


# grid() coloca los widgets en filas y columnas

# tk.Label(root, text="Etiqueta Grid 1").grid(row=0, column=0)
# tk.Label(root, text="Etiqueta Grid 2").grid(row=0,column=1)

# place() coloca los widgets con posiciones absolutas

# tk.Label(root, text="Etiqueta Place 1").place(x=50, y=50)
# tk.Label(root, text="Etiqueta Place 2").place(x=50, y=300)


root.mainloop()