from tkinter import *

window = Tk()
window.title("my first program ")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# Label
my_label = Label(text="label is Rohit", font=("Arial", 24, "bold"))
# my_label.pack(expand=True)
# my_label.pack(side= "left")
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

my_label["text"] = "new text"
my_label.config(text="New Text")

#button

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Clink me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="new button")
new_button.grid(column=2, row =0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
print(input.get())



window.mainloop()