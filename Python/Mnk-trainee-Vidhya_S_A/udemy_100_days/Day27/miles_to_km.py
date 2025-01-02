from tkinter import *



window=Tk()
window.minsize(width=500,height=300)
window.title("KiloMeter calculator")
window.config(padx=20,pady=20)


def calculate():
    miles=ent.get()
    km=1.609*float(miles)
    label1.config(text=f"{km}")




label=Label(text='Miles',font=('Arial',20,'bold'))
label.grid(column=3,row=0)

ent=Entry()
ent.grid(column=2,row=0)

label=Label(text="is equal to",font=('Arial',20,'bold'))
label.grid(column=1,row=1)

label1=Label(text='0')
label1.grid(column=2,row=1)

label=Label(text='Km',font=('Arial',20,'bold'))
label.grid(column=3,row=1)

but=Button(text="Calculate",command=calculate)
but.grid(column=2,row=3)







window.mainloop()
