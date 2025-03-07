import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Etiqueta 1", bg="red")
label1.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)

label2 = tk.Label(root, text="Etiqueta 2", bg="blue")
label2.place(relx=0, rely=0.1, relwidth=0.1, relheight=0.1)

label3 = tk.Label(root, text="Etiqueta 3", bg="red")
label3.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.1)

label4 = tk.Label(root, text="Etiqueta 4", bg="blue")
label4.place(relx=0, rely=0.3, relwidth=0.1, relheight=0.1)

label5 = tk.Label(root, text="Etiqueta 5", bg="red")
label5.place(relx=0.1, rely=0.3, relwidth=0.1, relheight=0.1)

label6 = tk.Label(root, text="Etiqueta 6", bg="blue")
label6.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.3)


root.mainloop()