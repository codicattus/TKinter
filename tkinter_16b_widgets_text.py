import tkinter as tk

def cambiar_color():
    text_area_1.tag_add("color_rojo", "1.0", "1.5")
    text_area_1.tag_configure("color_rojo", foreground="red")

root = tk.Tk()

text_area_1 = tk.Text(root, height=10, width=40)
text_area_1.pack(pady=20)
text_area_1.insert("1.0", "Este es un texto con formato aplicado.\n")

button = tk.Button(root, text="Cambiar color", command=cambiar_color)
button.pack(pady=10)


# Creamos el Frame que encapsulará el resto de widgets
frame = tk.Frame(root, width=300)
frame.pack(pady=40)

# Creamos el widget Text dentro de frame
text_area_2 = tk.Text(frame, wrap="word")
text_area_2.pack(side="left", fill="both", expand=True)

# Crear la barra de desplazamiento vertical
scrollbar = tk.Scrollbar(frame, command=text_area_2.yview, width="40")
scrollbar.pack(side="right",fill="y")  # La barra de desplazamiento va al lado derecho

# Vincular la barra de desplazamiento con el widget Text
text_area_2.config(yscrollcommand=scrollbar.set)

# Insertar texto para hacer que aparezca la barra de desplazamiento
for i in range(100):
    text_area_2.insert("end", f"Línea {i+1}\n")


root.mainloop()
