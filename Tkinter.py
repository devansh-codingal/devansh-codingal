from tkinter import *
from datetime import date

window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

lb1 = Label(text="Hi, there", fg="white", bg="blue", height=1, width=300)
lb2 = Label(text="Enter your full name", fg="white", bg="lightblue", height=1, width=100)
inp1 = Entry()

def display():
  name = inp1.get()
  
  message = "Welcome to the application \nToday's date is : "
  greeting = f"Hi, {name}\n"
  
  text_box.insert(END, greeting)
  text_box.insert(END, message)
  text_box.insert(END, date.today())
  
text_box = Text(height=3)

btn = Button(text="Submit", command=display, fg="white", bg="red", height=1)

lb1.pack()
lb2.pack()
inp1.pack()
text_box.pack()
btn.pack()

window.mainloop()