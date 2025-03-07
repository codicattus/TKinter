import tkinter as tk
from PIL import Image, ImageTk 

def toggle_password():
    if entry.cget("show") == "":
        entry.config(show="*")
    else:
        entry.config(show="")

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady=60)

entry = tk.Entry(frame, width=60,justify="center")
entry.pack(side="left")

img = Image.open("contrasena.png").resize((50, 50))
imagen = ImageTk.PhotoImage(img)


btn = tk.Button(frame,  image=imagen, compound="center",command=toggle_password)
btn.pack(side="right")


root.mainloop()