#Miles to kilometer convertor

from tkinter import *

#creating a window object
window = Tk()
window.title("Miles to kilometer convertor")
window.minsize(300,200)
window.config(padx=30,pady=30)

#creating labels using label class
label = Label(text = 'Enter miles :',font=('arial',10))
label.grid(column=1,row=1)

label1 = Label(text = 'Miles',font=('arial',10))
label1.grid(column=3,row=1)

label3 = Label()
label3.grid(column=2,row =3)

#creating input fields using entry class
input_box = Entry()
input_box.grid(column=2,row=1)

#creating buttons
def calculate():
    input = float(input_box.get())
    kilometer = round(input  * 1.609344)
    label3.config(text = f"{kilometer} kilometer")




button = Button(text='Calculate',command=calculate)
button.grid(column=2,row=2)













window.mainloop()