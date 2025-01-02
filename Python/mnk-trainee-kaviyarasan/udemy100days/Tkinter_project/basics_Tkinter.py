from tkinter import *

from uri_template import expand

window = Tk()

window.title("Title")
window.minsize(width=600,height=600)

lable = Label()


lable["text"] = "new text"
lable.config(text="new text")
lable.grid(column=0,row=0)


def button_():
    new_t = inputs.get()
    lable.config(text=new_t)

inputs = Entry(width=10)
inputs.grid(column=1,row=1)
inputs.get()
fred = Button(text="click me",fg="red", bg="blue",command=button_)
fred["fg"] = "red"
fred["bg"] = "blue"
fred.config(fg="red", bg="blue")
# print(fred.config())
fred.grid(column=2,row=2) # widget will appear only when after  pack() has called


window.mainloop() # interpreter runs an event loop tk.mainloop respond the event


