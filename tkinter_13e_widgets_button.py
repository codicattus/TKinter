import tkinter as tk

def mostrar_menu(event):
    menu.post(event.x_root, event.y_root)  # Muestra el menú en la posición del mouse

def on_key_press(event):
    print(f"Tecla presionada: {event.keysym}")

root = tk.Tk()

menu = tk.Menu(root, tearoff=0)                                                        # Crea un menú emergente.
menu.add_command(label="Opción 1", command=lambda: print("Opción 1 seleccionada"))     # Añade opciones al menú.
menu.add_command(label="Opción 2", command=lambda: print("Opción 2 seleccionada"))

btn = tk.Button(root, text="Menú")
btn.pack(pady=20)
btn.bind("<Button-3>",mostrar_menu)                                                   # Asocia el menú al botón derecho del mouse.

root.focus_set()                                                                       # Cambiamos el "foco" a root (o sea, la ventana principal)
root.bind("<KeyPress>", on_key_press)

root.mainloop()


#  Eventos de ratón comunes:
# ==========================
# Button-1: Botón izquierdo del ratón.
# Button-2: Botón del medio.
# Button-3: Botón derecho del ratón.

#  Eventos de teclado comunes:
# ============================
# <Return> o <Enter>: Presionar la tecla Enter (o Return).
# <Escape>: Presionar la tecla Escape.
# <Tab>: Presionar la tecla Tab (para navegar entre campos o widgets).
# <Control-Alt-Delete>: Una combinación de teclas que se puede asociar a un evento (si no está bloqueada por el sistema operativo).
# <KeyPress>: Cualquier tecla presionada.

# Eventos de ratón combinados:
# ============================
# <Control-Button-1>: Clic izquierdo del ratón mientras mantienes presionada la tecla Control.
# <Shift-Button-1>: Clic izquierdo del ratón mientras mantienes presionada la tecla Shift.
# <Alt-Button-1>: Clic izquierdo del ratón mientras mantienes presionada la tecla Alt.
# <Button-1><Button-2>: Combinación de clic izquierdo y medio.

# Otros eventos del ratón:
# ========================
# <Motion>: Movimiento del ratón dentro de un widget.
# <Enter>: El ratón entra en el área de un widget.
# <Leave>: El ratón sale del área de un widget.