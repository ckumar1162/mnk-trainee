from tkinter import *
from tkinter import messagebox

import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

mixed_items = letters + numbers + symbols

def gen_password():

    password_letter = [random.choice(letters) for _ in range(random.randint(6, 10))]
    password_numbers= [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list =password_letter + password_symbols + password_numbers
    random.shuffle(password_list)

    final_password =''.join(password_list)

    pass_entry.insert(0,final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# code for encrypting original password to encrypted password
def encrpt_pw(pw, key):
    encoded_pw=''
    for i in pw:
        shift_position=mixed_items.index(i) + key
        shift_position %= len(mixed_items)
        encoded_pw +=mixed_items[shift_position]

    return encoded_pw

def save():
    web=web_entry.get()
    uname=user_entry.get()
    passwords=pass_entry.get()
    shift_key=2

    if len(web) <=0 or len(passwords)<=0:
        messagebox.showerror(title='Error:',message="Please don't let any fields empty!")

    else:
        is_ok=messagebox.askokcancel(title=web,message=f"These are the fields entered: \nEmail: {uname} \n Password:{passwords}")
        if is_ok:
            encoded_password=encrpt_pw(passwords,shift_key)

            with open('data.txt','a') as data:
                data.write(f"{web} | {uname} | {encoded_password} \n")

                web_entry.delete(0,END)
                pass_entry.delete(0,END)

def login_check():
    web=web_entry.get()
    uname=user_entry.get()
    passwords=pass_entry.get()
    shift_key=2

    if len(web) <=0 or len(passwords)<=0:
        messagebox.showerror(title='Error:',message="Please don't let any fields empty!")
    else:
        with open('data.txt') as data:
            dats_in_file=data.readlines()





# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas =Canvas(height=200,width=200)
img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)


# Labels
website=Label(text='Website : ')
website.grid(column=0,row=1)

user_name=Label(text='Email/Username : ')
user_name.grid(column=0,row=2)


password=Label(text="Password : ")
password.grid(column=0,row=3)

# Entries
web_entry=Entry(width=35)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

user_entry=Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0,'ram23@gamil.com')

pass_entry=Entry(width=21)
pass_entry.grid(column=1,row=3)

#Buttons
generate_pass=Button(text="Generate Password",command=gen_password)
generate_pass.grid(column=2,row=3)

add=Button(text="Add",width=25,command=save)
add.grid(column=1,row=4,columnspan=2)

# Login
login = Button(text='Login', width=25, command=login_check)
login.grid(column=1, row=5, columnspan=2)



window.mainloop()
