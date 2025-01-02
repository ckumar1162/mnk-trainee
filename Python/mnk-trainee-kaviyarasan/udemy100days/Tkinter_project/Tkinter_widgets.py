from tkinter import *

# to create a new window and configuration
window = Tk()
window.title("(widgets example)")
window.minsize(width=600, height=500)

# lables
lable = Label()
lable.config(text="hi")
lable.pack()

# buttons
def action():
    # print("do something")
    lable.config(text="kavi")
# calls action() when something
button = Button(text="click me", command=action)
button.pack()

# entriesaa
entry = Entry(width=30)
# add some text to begin with
entry.insert(END, string="some text to begin with.")
entry.pack()

# text
text = Text(height=5,width=30)
# puts cursor in textbox.
text.focus()
# adds some text to begin with.
text.insert(END,"example pf multi-line text entry.")
# get's current values in textbox at line1, charater 0
text.get("1.0",END)
text.pack()

# spinbox
def spinbox_used():
    # get the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

# scale
# called with curent scale value.
def scale_used(values):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# checkbutton
def checkbuttton_used():
    #prints 1 if on button checked,
    # otherwise 0.
    print(checked_state.get())
# variable to hold on the checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbuttton = Checkbutton(text="is on?",variable=checked_state,command=checkbuttton_used)
checked_state.get()
checkbuttton.pack()

# radiobutton
def radio_used():
    print(radio_state.get())
# variable to hold on to which radio button values is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text= "option2",value=1, variable= radio_state,command = radio_used)
radiobutton2 = Radiobutton(text="option3",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# listbox
def listbox_used(event):
    #gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert((fruits.index(item)),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()