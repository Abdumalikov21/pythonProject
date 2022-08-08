from tkinter import*
from time import strftime
root = Tk()
root.title("Soat")
lbl = Label(root, font=("caliber", 48, "bold"), bg ="purple", fg ="white")
def time():
    string=strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)
lbl.pack()


time()

root.mainloop()