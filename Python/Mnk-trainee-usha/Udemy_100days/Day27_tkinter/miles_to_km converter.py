from tkinter import *

tk=Tk()

def miles_to_km():
    miles=float(textbox.get())
    km=round(miles*1.609)
    label3.config(text=f"{km}")

tk.title("Mile to Km Converter")
tk.minsize(width=200,height=200)
tk.config(padx=50,pady=50)

#adding textbox for enrty
textbox=Entry(width=7)
textbox.grid(column=1,row=0)

label1=Label(text="Miles")
label1.grid(column=2,row=0)

label2=Label(text="is equal to")
label2.grid(column=0,row=1)

label3=Label(text="0")
label3.grid(column=1,row=1)

label4=Label(text="Km")
label4.grid(column=2,row=1)

button=Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)

tk.mainloop()