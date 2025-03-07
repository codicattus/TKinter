import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack(pady=20)


def cambiar_estado():
    if entry.cget("state") == "normal":
        entry.config(state="readonly") # Pasar a solo lectura
        btn_borrar.config(state="disabled")
    else:
        entry.config(state="normal")
        btn_borrar.config(state="normal") # Pasar a modo escritura

def borrar_texto():
    entry.delete(0, tk.END)  # Borra el contenido


btn_estado = tk.Button(root, text="Cambiar estado", command=cambiar_estado)
btn_estado.pack(pady=10)
btn_borrar = tk.Button(root, text="Borrar texto", command=borrar_texto)
btn_borrar.pack(pady=10)


root.mainloop()


