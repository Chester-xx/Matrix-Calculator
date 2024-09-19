import customtkinter as c 

# implemeent into gui to pass floats into main

root = c.CTk()
root.geometry("300x200")
root.title("Test")

global var
var = c.DoubleVar()

ent = c.CTkEntry(master=root, textvariable=var)
ent.pack()
btn = c.CTkButton(master=root, command = lambda : inc(var))
btn.pack()



def inc(var) -> None :
    x : float = float(var.get())
    x += 1
    
    if x % 1 == 0 :
        var.set(f"{x:.0f}")
    
    else: 
        var.set(f"{x:.2f}")

root.mainloop()

def _2x2() -> None :

# Above release Pre v1.0.2 test code