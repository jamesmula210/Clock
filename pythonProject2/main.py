from tkinter.ttk import *
from tkinter import *

from time import strftime

admin = Tk()

admin.title("Watch")
tag = Label(font=("Comic  Sans", 90),background="aqua", foreground="green")
tag.pack(anchor="center")


def get_time():
    string = strftime("%H:%M:%S %p")
    tag.config(text=string)
    tag.after(1000, get_time)


get_time()
mainloop()



