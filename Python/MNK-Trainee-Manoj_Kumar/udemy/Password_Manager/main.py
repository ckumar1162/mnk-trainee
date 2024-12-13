import os.path
from tkinter import *
from tkinter import messagebox
import string
import random
import pandas


screen = Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20, bg="#f7f5dd")

def pass_generator():
    characters = string.digits+string.ascii_letters+string.punctuation
    password = "".join(random.choice(characters) for i in range(6))
    password_inp.delete(0,END)
    password_inp.insert(0,password)

def get_data():
    pas = password_inp.get()
    web = web_inp.get()
    email = email_inp.get()
    return [web,email,pas]
def delete_data():
    password_inp.delete(0,END)
    email_inp.delete(0,END)
    web_inp.delete(0,END)
def add_data():
    web_data,email_data,pass_data = get_data()
    if not web_data or not email_data or not pass_data:
        messagebox.showerror("Error","Enter Every Field")
        return
    new_entry = {"website":web_data,"email":email_data,"password":pass_data}
    df = pandas.DataFrame([new_entry])
    json_file = "data.json"
    if os.path.exists(json_file):
        existing_file = pandas.read_json(json_file)
        updated_data = pandas.concat([existing_file,df],ignore_index=True)
        updated_data.to_json(json_file,indent=4)
        messagebox.showinfo("Success","Data Inserted Successfully")
        delete_data()

    else:
        df.to_json(json_file,indent=4)
        delete_data()



canvas = Canvas(width=200, height=200, bg="#f7f5dd", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website", font=("Arial", 12, "bold"), bg="#f7f5dd", fg="#333")
website.grid(row=1, column=0, pady=5)

web_inp = Entry(width=35, highlightbackground="#d3d3d3", highlightthickness=1)
web_inp.grid(row=1, column=1, columnspan=2, pady=5)
web_inp.focus()

email_label = Label(text="Email", font=("Arial", 12, "bold"), bg="#f7f5dd", fg="#333")
email_label.grid(row=2, column=0, pady=5)

email_inp = Entry(width=35, highlightbackground="#d3d3d3", highlightthickness=1)
email_inp.grid(row=2, column=1, columnspan=2, pady=5)

password_label = Label(text="Password", font=("Arial", 12, "bold"), bg="#f7f5dd", fg="#333")
password_label.grid(row=3, column=0, pady=5)

password_inp = Entry(width=21, highlightbackground="#d3d3d3", highlightthickness=1)
password_inp.grid(row=3, column=1, pady=5)


pass_generator_btn = Button(text="Generate",command=pass_generator, bg="#4caf50", fg="white", font=("Arial", 10, "bold"), highlightthickness=0)
pass_generator_btn.grid(row=3, column=2, pady=5)

add_btn = Button(text="Add",command=add_data, width=36, bg="#2196f3", fg="white", font=("Arial", 12, "bold"), highlightthickness=0)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

screen.mainloop()
