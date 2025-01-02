from tkinter import *

window = Tk()
window.config(padx=50,pady=50)
window.title("Mile Km converter")

entry_mile = Entry(width=10)
entry_mile.insert(END,string="0")
entry_mile.grid(column=2,row=0)

lable1 = Label(width=10)
lable1.config(text="miles")
lable1.grid(column=3,row=0)

lable2 = Label()
lable2.config(text="is equal to")
lable2.grid(column=0,row=1)

lable_result = Label()
lable_result.grid(column=2,row=1)

lable4 = Label()
lable4.config(text="Km")
lable4.grid(column=3,row=1)


def mile_to_km():
    mile =  float(entry_mile.get())
    km = mile * 1.609
    lable_result.config(text=F"{km}")

def km_to_mile(km):
    return km * 0.621371


km_calculate = Button()
km_calculate.config(text="Calculate",command=mile_to_km)
km_calculate.grid(column=2,row=3)


window.mainloop()
