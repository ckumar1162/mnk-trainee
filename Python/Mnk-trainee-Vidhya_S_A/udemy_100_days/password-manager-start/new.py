from tkinter import *
from tkinter import messagebox
import random
import bcrypt  # Library for hashing passwords
import pyperclip

# ----------------------------- HASH PASSWORD ----------------------------- #
def hash_password(password):
    
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #encode convert into bytes
    return hashed_pw.decode('utf-8') # deocode will convert bytes into string

# ----------------------------- VERIFY PASSWORD ----------------------------- #
def verify_password(hashed_password, input_password):

    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pw.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_input = web.get()
    user_input = user.get()
    password1 = pw.get()

    if len(website_input) == 0 or len(password1) == 0:
        messagebox.showinfo(title="OOPS!!!", message="Please don't leave any fields empty")
    else:
        hashed_pw = hash_password(password1)  # Hash the password
        msg_box = messagebox.askokcancel(
            title=website_input,
            message=f'These are the details you entered:\nEmail: {user_input}\nPassword: {password1}\nIs it OK to save?'
        )
        if msg_box:
            try:
                with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\password-manager-start\new_data.txt", 'a') as file:
                    file.write(f"{website_input} | {user_input} | {hashed_pw}\n")
                web.delete(0, END)
                pw.delete(0, END)
            except FileNotFoundError:
                messagebox.showerror(title="Error", message="No such file found")

# ---------------------------- LOGIN FUNCTION ------------------------------- #
def login():
    web_input = web.get()
    user_input = user.get()
    password_input = pw.get()

    if len(web_input) == 0 or len(user_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(message="Please fill the required fields")
        return

    try:
        with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\password-manager-start\new_data.txt") as data_file:
            content = data_file.readlines()
    except FileNotFoundError:
        messagebox.showerror(message="No such file found")
        return

    for data in content:
        saved_website, saved_user, saved_hashed_pw = [item.strip() for item in data.strip().split('|')]

        if web_input == saved_website and user_input == saved_user:
            if verify_password(saved_hashed_pw, password_input):  # Verify hashed password
                messagebox.showinfo(message="Login Successful")
                return
            else:
                messagebox.showerror(message="Invalid password")
                return

    messagebox.showerror(message="No matching credentials found!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create canvas for logo
canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file=r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\password-manager-start\logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

# Create labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create entry fields
web = Entry(width=39)
web.grid(column=1, row=1, columnspan=2)
web.focus()

user = Entry(width=39)
user.grid(column=1, row=2, columnspan=2)
user.insert(END, 'vidhya@gmail.com')

pw = Entry(width=21)
pw.grid(column=1, row=3)

# Create buttons
generate = Button(text='Generate Password', command=generate_password)
generate.grid(column=2, row=3)

add = Button(text='Add', width=34, command=save_data)
add.grid(column=1, row=4, columnspan=2)

login_btn = Button(text='Login', width=34, command=login)
login_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
