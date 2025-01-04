import pandas as pd
from tkinter import *
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

def encrypt_password(password):
    encrypted = "".join(chr(ord(char) + 7) for char in password)
    return encrypted

def decrypt_password(encrypted_password):
    decrypted = "".join(chr(ord(char) - 7) for char in encrypted_password)
    return decrypted

def generate_password():
    password = []
    for char in range(0, 4):
        password += choice(letters)
    for sym in range(0, 2):
        password += choice(symbols)
    for num in range(0, 2):
        password += choice(numbers)
    shuffle(password)
    password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save_details():
    website = website_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not email or not username or not password:
        status_label.config(text="All fields are required", fg="red")
        return

    encrypted_password = encrypt_password(password)

    new_entry = {
        "Website Name": website,
        "Username": username,
        "Email": email,
        "Password": encrypted_password
    }

    try:
        data = pd.read_csv("user_data.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=["Website Name", "Username", "Email", "Password"])

    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
    data.to_csv("user_data.csv", index=False)

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    status_label.config(text="Details saved successfully", fg="green")

def login():
    website = website_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or (not email and not username) or not password:
        status_label.config(text="Website, email, username, and password are required", fg="red")
        return

    try:
        data = pd.read_csv("user_data.csv")
        if not data.empty:
            user_data = data[(data["Website Name"] == website) &
                             ((data["Email"] == email) | (data["Username"] == username))]

            if not user_data.empty:
                saved_password = decrypt_password(user_data.iloc[0]["Password"])
                if saved_password == password:
                    status_label.config(text="Successfully logged in", fg="green")
                else:
                    status_label.config(text="Incorrect login details", fg="red")
            else:
                status_label.config(text="Incorrect login details", fg="red")
        else:
            status_label.config(text="No user data found. Please add user first", fg="red")
    except FileNotFoundError:
        status_label.config(text="No user data found. Please add user first", fg="red")

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

Label(window, text="Website:", fg="blue").grid(row=1, column=0)
Label(window, text="Username:").grid(row=2, column=0)
Label(window, text="Email:").grid(row=3, column=0)
Label(window, text="Password:").grid(row=4, column=0)

website_entry = Entry(window, width=40)
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = Entry(window, width=40)
username_entry.grid(row=2, column=1, columnspan=2)

email_entry = Entry(window, width=40)
email_entry.grid(row=3, column=1, columnspan=2)

password_entry = Entry(window, width=30)
password_entry.grid(row=4, column=1)

Button(window, text="Generate Password", command=generate_password).grid(row=4, column=2)
Button(window, text="Add", width=36, command=save_details).grid(row=5, column=1, columnspan=2)
Button(window, text="Login", width=36, command=login).grid(row=6, column=1, columnspan=2)

status_label = Label(window, text="", fg="green")
status_label.grid(row=7, column=1, columnspan=2)

window.mainloop()
