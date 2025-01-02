from tkinter import *

window=Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)

# Label

lab=Label(text='My label',font=('Arial',24,'bold'))
lab.grid(column=0,row=0)

def clicked_button():
    new_text=input.get()
    lab.config(text=new_text)

# Button
b=Button(text='click me',command=clicked_button)
b.grid(column=1,row=1)

but=Button(text='new button')
but.grid(column=3,row=0)

# Entry
input=Entry(width=10)
input.grid(column=4,row=3)








window.mainloop()