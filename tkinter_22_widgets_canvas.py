import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Canvas")

canvas = tk.Canvas(root, width=1200, height=800, bg="white")
canvas.pack()

# Dibujar línea
canvas.create_line(100, 50, 1100, 50, fill="red", width=5)

# Dibujar rectángulo
canvas.create_rectangle(100, 130, 1100, 330, fill="blue")

# Dibujar círculo
canvas.create_oval(100, 410, 200, 510, fill="red")
canvas.create_oval(100, 520, 200, 620, fill="yellow")
canvas.create_oval(100, 630, 200, 730, fill="green")

# Dibujar texto
canvas.create_text(300, 570, text="Semáforo", font=("Arial", 14))

root.mainloop()


# Conceptos básicos de Canvas:

# Crear un lienzo: canvas = tk.Canvas(root, width=400, height=300, bg="white")

# Dibujar elementos:
# Líneas: canvas.create_line(x1, y1, x2, y2, fill="red", width=2)
# Óvalos/Círculos: canvas.create_oval(x1, y1, x2, y2, fill="blue")
# Rectángulos: canvas.create_rectangle(x1, y1, x2, y2, fill="green")
# Texto: canvas.create_text(x, y, text="Hola", font=("Arial", 14))

# Imágenes: Se puede cargar imágenes con PhotoImage y mostrarlas con canvas.create_image(x, y, image=img, anchor="nw")

# Valores comunes de anchor:

# Valor de anchor	               Posición que se alinea con (x, y)
# ---------------------------------------------------------------------- #
# "center"	                      Centro de la imagen (Por defecto)
# "nw"	                          Esquina superior izquierda
# "ne"	                          Esquina superior derecha
# "sw"	                          Esquina inferior izquierda
# "se"	                          Esquina inferior derecha
# "n"	                          Centro del borde superior
# "s"	                          Centro del borde inferior
# "w"	                          Centro del borde izquierdo
# "e"	                          Centro del borde derecho