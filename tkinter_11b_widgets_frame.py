import tkinter as tk

root = tk.Tk()
root.geometry("1600x800")



#################
# Usando pack() #
#################



# frame_left = tk.Frame(root, bg="red", width=400)
# frame_left.pack(side="left", fill="y")

# frame_right = tk.Frame(root, bg="blue")
# frame_right.pack(side="right", fill="both", expand=True) 



#################
# Usando grid() #
#################


# root.columnconfigure(0, weight=0)  
# root.columnconfigure(1, weight=1)  
# root.rowconfigure(0, weight=1)  
 

# frame_left = tk.Frame(root, bg="red", width=400, height=1000)
# frame_left.grid(row=0, column=0, sticky="nsew")

# frame_right = tk.Frame(root, bg="blue")
# frame_right.grid(row=0, column=1, sticky="nsew") 


##################
# Usando place() #
##################

frame_left = tk.Frame(root, bg="red")
frame_left.place(relx=0, rely=0, relwidth=0.4, relheight=1)

frame_right = tk.Label(root, bg="blue")
frame_right.place(relx=0.4, rely=0, relwidth=1, relheight=1)



root.mainloop()

