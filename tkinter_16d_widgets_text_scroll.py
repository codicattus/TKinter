import tkinter as tk

def move_up():
    # Mover el texto hacia arriba (desplazamiento)
    text_area.yview_scroll(-1, "units")

def move_down():
    # Mover el texto hacia abajo (desplazamiento)
    text_area.yview_scroll(1, "units")

root = tk.Tk()

# Crear un Frame para contener el Text y los botones de desplazamiento
frame = tk.Frame(root, width=300, height=100)
frame.pack(padx=20, pady=20)

# Crear el widget Text dentro del frame
text_area = tk.Text(frame, wrap="word", height=10, width=40)
text_area.pack(side="left", fill="both", expand=True)

# Insertar texto para hacer que aparezca el desplazamiento
for i in range(100):
    text_area.insert("end", f"Línea {i+1}\n")

# Crear botones personalizados para desplazamiento hacia arriba y hacia abajo
up_button = tk.Button(frame, text="↑", command=move_up, width=4, height=2, bg="lightblue", font=("Arial", 14))
down_button = tk.Button(frame, text="↓", command=move_down, width=4, height=2, bg="lightblue", font=("Arial", 14))

# Ubicar los botones en el Frame
up_button.pack(side="top",fill="y",expand=True)
down_button.pack(side="bottom", fill="y",expand=True)

root.mainloop()



# Opciones de wrap en Text

# El parámetro wrap en el widget Text controla cómo se ajustan las líneas de texto cuando alcanzan el final del ancho disponible. 
# Las opciones para wrap son:

# wrap="none":
# No se hace ningún ajuste automático de línea. 
# Si una palabra no cabe en el espacio disponible, simplemente se cortará a la mitad, lo que generalmente no es lo que se desea. 
# El contenido continuará en una única línea horizontal y habrá que desplazarse para verlo por completo.

# wrap="word":

# Esta opción ajusta el texto para que se haga un salto de línea solo cuando una palabra no cabe completamente. 
# Si una palabra es demasiado larga para caber en el espacio disponible, se mueve completamente a la siguiente línea, evitando cortar las palabras.

# wrap="char":
# Esta opción realiza el salto de línea en cualquier lugar, incluso en medio de las palabras. 
# Si el texto no cabe en el ancho del widget, el salto de línea se producirá a nivel de caracteres, independientemente de si la palabra está completa o no. 

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Opciones de yview_scroll y el uso de unit:

# El método yview_scroll permite desplazar el contenido del widget Text en dirección vertical (hacia arriba o hacia abajo) de acuerdo con la cantidad que se indique.
# El primer parámetro de yview_scroll es el número de "unidades" a desplazar, y el segundo parámetro es la unidad de medida. 


# Opciones de unidades para yview_scroll:

# "units":
# Desplaza el texto por un número determinado de unidades, donde cada unidad corresponde a la altura de una línea de texto (una línea completa de texto desplazada). 

# "pages":

# Desplaza el texto por una "página" completa. Una página es el área visible del widget Text. Si la ventana es lo suficientemente grande y se puede ver más de una línea de texto a la vez, el desplazamiento será el tamaño completo de la pantalla visible (el espacio en la ventana que ocupa el widget Text). Esto permite hacer desplazamientos más largos, por ejemplo, a través de varias líneas de texto de una sola vez.

# "moveto":
# Permite desplazar el texto a una posición específica. 
# El parámetro que se pasa con "moveto" es un valor entre 0.0 y 1.0, que indica la proporción del texto que se debe mostrar, siendo:

#  -------- 0.0 = inicio del texto.
#  -------- 0.5 = mitad del texto.
#  -------- 1.0 = final del texto.
