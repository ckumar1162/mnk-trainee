from tkinter import *
#practice
tk = Tk()

tk.title("My First GUI Program")
tk.minsize(width=500, height=300)
tk.config(padx=100,pady=200)

def button_clicked():
    print("I Got Clicked")
    input=textbox.get()
    label.config(text=input)

# to create Label
label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
label.grid(column=0,row=0)
label["text"]="My Text"


# to create button
button=Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

# to create a text box or entry
textbox=Entry(width=10)
print(textbox.get())# to write to into a box
textbox.grid(column=3,row=2)

button2=Button(text="Button")
button2.grid(column=2,row=0)

tk.mainloop()
