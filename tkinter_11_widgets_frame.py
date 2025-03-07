import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, bg="gray", width=400, height=800, relief="flat", bd=5)
frame.pack()


root.mainloop()


# Principales opciones de configuración

# bg: Color de fondo.
# width: Ancho del frame (opcional, ajustable automáticamente).
# height: Altura del frame.
# relief: Tipo de borde ("flat", "raised", "sunken", "ridge", "solid", "groove").
# bd: Tamaño del borde.