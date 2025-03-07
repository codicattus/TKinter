import tkinter as tk
from PIL import Image, ImageTk  # Necesita instalar Pillow: `pip install pillow`

root = tk.Tk()

img = Image.open("icono.png").resize((50, 50))  # Cargar y redimensionar imagen
img_tk = ImageTk.PhotoImage(img)

btn = tk.Button(root, text=" Enviar", image=img_tk, compound="bottom",  width=300, height=120)  # Botón con imagen
btn.pack(pady=20)

root.mainloop()


# Las imágenes deben estar en un formato soportado (PNG, JPG, GIF).
# PhotoImage de Tkinter solo admite GIF y PNG, para otros formatos se usa PIL.ImageTk.PhotoImage.
# La imagen debe mantenerse en una variable, si se asigna dentro de Button, se eliminará de la memoria.

# Opciones de compound
# Cambiar la posición de la imagen respecto al texto:

# "top" →    Imagen arriba, texto abajo.
# "bottom" → Imagen abajo, texto arriba.
# "left" →   Imagen a la izquierda, texto a la derecha.
# "right" →  Imagen a la derecha, texto a la izquierda.
# "center" → Imagen y texto superpuestos (por defecto).
# "none" →   Solo muestra la imagen, ignora el texto.

