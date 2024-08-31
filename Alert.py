from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Anti-virus software")
root.geometry('200x200')
def msg():
    #messagebox.showwarning("Alert", "A virus is found!")
    messagebox.askquestion("Query", "A virus has been detected. Do you want to continue?")

btn = Button(master=root, text="Scan for virus", command=msg)
btn.place(x=40, y=80)

root.mainloop()