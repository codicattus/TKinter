import tkinter as tk

def activar():
    btn.config(state="normal")

def desactivar():
    btn.config(state="disabled")

root = tk.Tk()

btn = tk.Button(root, text="No puedes hacer clic", state="disabled")
btn.pack(pady=10)

btn_activar = tk.Button(root, text="Activar botón", command=activar)
btn_activar.pack(pady=10)

btn_desactivar = tk.Button(root, text="Desctivar botón", command=desactivar)
btn_desactivar.pack(pady=10)

root.mainloop()
