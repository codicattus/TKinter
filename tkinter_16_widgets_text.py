import tkinter as tk

root = tk.Tk()

text_area_1 = tk.Text(root, width=40, height=10, wrap="word")
text_area_1.pack(pady=20)


text_area_1.insert(tk.END, "Este es un área de texto multilinea.\nSe pueden escribir varias líneas.")


text_area_2 = tk.Text(root, height=10, width=40)
text_area_2.pack(pady=20)

text_area_1.tag_configure("plus", font=("Helvetica", 16, "bold"))
text_area_2.tag_configure("negrita", font=("Helvetica", 12, "bold"))

text_area_2.insert(tk.END, "Texto normal, ")
text_area_2.insert(tk.END, "Texto en negrita", "negrita")
text_area_2.insert(tk.END, " y más texto normal.\n")

text_area_1.insert(tk.END, "\nNuevo texto añadido al final.\n", "plus")
text_area_1.insert("1.0", "Texto al principio.\n",)
text_area_1.see("1.5")

text_area_3 = tk.Text(root, height=10, width=40)
text_area_3.pack(pady=20)
for i in range(1, 201):
    text_area_3.insert(tk.END, f"Línea {i}\n")

text_area_3.see("150.0")






root.mainloop()



# Opciones comunes de Text:

# width:  El ancho del área de texto en caracteres.
# height: La altura del área de texto en líneas.
# wrap:   Controla cómo se hace el ajuste de texto ("none", "char", "word").
#           --- "none": El texto no se ajusta, se extiende más allá del área visible.
#           --- "char": El texto se ajusta a las líneas por caracteres.
#           --- "word": El texto se ajusta por palabras (esto es lo más común).
# font:   Define el tipo y tamaño de la fuente.
# bg:     Color de fondo del widget.
# fg:     Color del texto


# Algunos métodos útiles:

# tag_add(tag, start, end):        Asocia un tag a una parte específica del texto.
# **tag_configure(tag, options):   Configura las opciones del tag, como el color, la fuente, etc.
# see(index):                      Mueve la vista del widget hasta la posición indicada por index.

# En Tkinter, cuando trabajamos con el widget Text, los índices se representan como fila.columna.

# Índices especiales:
#  - "end": Hace referencia al final del contenido.
#  - "insert": Hace referencia a la posición del cursor (donde se está escribiendo).
#  - "current": Hace referencia a la posición del cursor cuando se hace clic en el texto.