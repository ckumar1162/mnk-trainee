from tkinter import *
from tkinter import messagebox
import random
tk=Tk()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    textbox3.insert(0,password)
    #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website=textbox1.get()#get() method used to take value from entry widget
    email=textbox2.get()
    password=textbox3.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Ooops",message="Please make sure you haven't left any fields empyt.")
    else:
        #to add messagebox
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details enterd: \nEmail: {email} \nPassword: {password} ]n Is it okay to save ")
        if is_ok:
            with open("data.txt","a")as data:
                data.write(f"{website} | {email} | {password}\n")
                textbox1.delete(0,END)
                textbox2.delete(0, END)
                textbox3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
tk.title("Password Manager")
tk.config(padx=50,pady=50)

canvas=Canvas(width=150,height=150)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)

website_lebal=Label(text="website:")
website_lebal.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

textbox1=Entry(width=39)
textbox1.grid(column=1,row=1,columnspan=2)
textbox1.focus()

textbox2=Entry(width=39)
textbox2.grid(column=1,row=2,columnspan=2)
textbox2.insert(0,"abcd@gmail.com")#from this email will be pre-populated in the email textbox

textbox3=Entry(width=21)
textbox3.grid(column=1,row=3)

password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(column=2,row=3)

add_button=Button(text="Add",width=33,command=save)
add_button.grid(column=1,row=4,columnspan=2)

tk.mainloop()