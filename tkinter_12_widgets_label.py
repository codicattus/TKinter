import tkinter as tk
import tkinter.font

root = tk.Tk()
root.geometry("1600x800")





label = tk.Label(root, text="Etiqueta 1", font=("Arial", 14), fg="white", bg="blue")
label.pack(pady=80)
label1 = tk.Label(root, text="Etiqueta 2", font=("Times New Roman", 18, "underline"), fg="sandy brown", bg="medium purple")
label1.pack(pady=80)
label2 = tk.Label(root, text="Etiqueta 3", font=("Courier", 22, "overstrike"), fg="black", bg="dodger blue")
label2.pack(pady=80)




root.mainloop()











# Configuraciones principales
# text: Texto a mostrar.
# font: Fuente y tamaño (("Arial", 12, "bold")).
# fg: Color del texto.
# bg: Color de fondo.
# padx, pady: Espaciado interno.
# anchor: Posicionamiento del texto dentro del label ("center", "w", "e", etc.).

# --------------------------------------------------------------------------------- #

# Formato de font

# font=("Tipo de fuente", Tamaño, "Estilo")
# Tipo de fuente: Nombre de la fuente (Arial, Helvetica, Times New Roman, Courier, etc.).
# ***** tkinter.font.families()  ---->  Lista de fuentes disponibles en el sistema   ***** Necesita importar tkinter.font
# Tamaño: Número entero.
# Estilo (opcional): "bold", "italic", "underline", "overstrike".

# --------------------------------------------------------------------------------- #

# Colores en Label (fg y bg)

# fg="color" → Color del texto (foreground).
# bg="color" → Color del fondo (background).

# Maneras de definir colores

# Nombre del color: "red", "blue", "yellow", "green", "black", "white", etc.
# Lista de nombres de colores que se pueden usar ---> https://www.w3.org/TR/css-color-3/#svg-color
# Código hexadecimal: "#FF5733" (formato #RRGGBB).
# Sistema RGB (requiere tkinter.colorchooser):