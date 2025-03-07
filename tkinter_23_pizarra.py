import tkinter as tk

def draw(event):
    """Dibuja en el lienzo con el grosor y color seleccionado"""
    x, y = event.x, event.y
    width = slider_value.get()
    canvas.create_oval(x - width, y - width, x + width, y + width, fill=current_color, outline="")

def show_value(valor):
    """Actualiza la etiqueta y la vista previa del grosor"""
    update_preview()

def update_preview():
    """Actualiza el círculo de vista previa del lápiz en canvas_barra"""
    canvas_barra.delete("preview")
    width = slider_value.get()
    x, y = 40, 40  # Ubicación a la izquierda
    canvas_barra.create_oval(x - width, y - width, x + width, y + width, fill=current_color, outline="", tags="preview")

def change_color(color):
    """Cambia el color del lápiz y la vista previa"""
    global current_color
    current_color = color
    update_preview()

def clear_canvas():
    """Borra todo el contenido del lienzo."""
    canvas.delete("all")

root = tk.Tk()
root.title("Pizarra interactiva")

# Lienzo principal donde se dibuja
canvas = tk.Canvas(root, width=1200, height=600, bg="white", relief="solid", bd=5)
canvas.pack(pady=40)

# Lienzo barra para vista previa del lápiz y controles
canvas_barra = tk.Canvas(root, width=1200, height=80, bg="AntiqueWhite1", relief="solid", bd=5)
canvas_barra.pack()

# Variable del slider
slider_value = tk.DoubleVar(value=2)

# Slider para cambiar el grosor del lápiz
slider = tk.Scale(root, 
                  from_=1, 
                  to=10, 
                  orient="horizontal", 
                  variable=slider_value, 
                  command=show_value, 
                  width=40, 
                  length=1200, 
                  bd=3
                  )

slider.pack(pady=10)

# Botones de selección de color
colors = [
    ("Negro", "black"), 
    ("Rojo", "red"), 
    ("Azul", "blue")]

x_pos = 400  # Ajusta según necesidad
y_pos = 40   # Centrado en canvas_barra

for text, color in colors:
    btn = tk.Button(canvas_barra, text=text, bg=color, fg="white", width=6, command=lambda c=color: change_color(c))
    canvas_barra.create_window(x_pos, y_pos, window=btn)
    x_pos += 160  # Ajuste del espacio entre botones

# Botón para borrar el canvas
btn_clear = tk.Button(root, text="Borrar", bg="white", fg="black", width=8, command=clear_canvas)
canvas_barra.create_window(x_pos+160, y_pos, window=btn_clear)

# Color inicial
current_color = "black"

# Evento de dibujo
canvas.bind("<B1-Motion>", draw)

# Dibujar la vista previa inicial
update_preview()

root.mainloop()

