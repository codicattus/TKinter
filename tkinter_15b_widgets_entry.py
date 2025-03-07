import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=20)

def mostrar_texto():
    texto = entry.get()  # Obtiene el texto ingresado
    print("Texto ingresado:", texto)
    entry.delete(0, tk.END)  # Borra el contenido

btn = tk.Button(root, text="Obtener texto", command=mostrar_texto)
btn.pack(pady=10)

root.mainloop()
