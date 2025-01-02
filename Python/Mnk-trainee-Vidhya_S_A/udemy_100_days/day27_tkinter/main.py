import tkinter

window = tkinter.Tk()
window.title("PRACTICE GUI")
window.minsize(400,400)

#creating labels using label class
new_label = tkinter.Label(text="Hello everyone!!!!")
new_label.pack() # pack method is used to place the label into the screen  

# access the keyword as same as accessing in dictionary 
new_label['text'] = "good morning "
#or we can also update it as 
new_label.config(text = "Good morning ")

def greetings():
    
    new_text = input.get()
    new_label.config(text = f"good morning {new_text}")
    



#credating buttons
# button = tkinter.Button(text = "click",command=greetings) #command keyword takes the function name as value
# button.pack()

button = tkinter.Button(text = "click",command=greetings) #command keyword takes the function name as value
button.grid(column=1,row=1)
#entry class : input field 

input = tkinter.Entry()
input.pack()


window.mainloop() # this mainloop will keep the screen on 