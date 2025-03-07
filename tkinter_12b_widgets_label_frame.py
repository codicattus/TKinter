import tkinter as tk

root = tk.Tk()

frame = tk.LabelFrame(root, text="Contenedor", padx=20, pady=20)
frame.pack(pady=20)

label = tk.Label(frame, text="Texto con padding interno", bg="yellow", font=("Arial", 12))
label.pack()

root.mainloop()
