import tkinter as tk
from PIL import Image, ImageTk  # Necesita instalar Pillow: `pip install pillow`

root = tk.Tk()

def on_enter(event):
    btn.config(bg="red", fg="black", relief="raised")  # Cambia color y relieve

def on_leave(event):
    btn.config(bg="magenta", fg="white", relief="flat")  # Restaura el estado normal

# btn = tk.Button(root, text="Enviar", bg="blue", fg="white", width=15, height=2, relief="flat", highlightthickness=0)
# btn.pack(pady=20)

# btn.bind("<Enter>", on_enter)  # Detecta cuando el ratón entra
# btn.bind("<Leave>", on_leave)  # Detecta cuando el ratón sale

btn = tk.Button(
    root, text="Enviar",
    bg="magenta", fg="black", 
    activebackground="red", activeforeground="white",
    width=15, height=2, relief="flat"
)

btn.pack(pady=20)

root.mainloop()