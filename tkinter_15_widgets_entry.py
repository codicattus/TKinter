import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack(pady=20)

entry_2 = tk.Entry(root, 
                 font=("Arial", 14),    # Fuente y tamaño del texto
                 fg="blue",             # Color del texto
                 bg="lightgray",        # Color de fondo
                 width=25,              # Ancho del campo
                 justify="center",      # Alineación del texto (left, center, right)
                 show="$")              # Oculta el texto (útil para contraseñas)
entry_2.pack(pady=20)


root.mainloop()
