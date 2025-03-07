import tkinter as tk

root = tk.Tk()

root.geometry("400x200")  # Para ver mejor los efectos

# Configuramos filas y columnas para que se expandan

# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)

# Widget normal
label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label1.grid(row=0, column=0, sticky="nsew")

# Widget que ocupa 2 filas
label2 = tk.Label(root, text="Etiqueta 2", bg="blue")
label2.grid(row=0, column=1, rowspan=2, sticky="nsew")

# Widget que ocupa 2 columnas
label3 = tk.Label(root, text="Etiqueta 3 (columnspan=2)", bg="green")
label3.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()
