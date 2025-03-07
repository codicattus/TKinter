import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="")

root = tk.Tk()
canvas = tk.Canvas(root, width=1200, height=600, bg="white")
canvas.pack(pady=40)

canvas.bind("<B1-Motion>", draw)  # Detectar el movimiento del ratón con el botón izquierdo presionado

root.mainloop()
