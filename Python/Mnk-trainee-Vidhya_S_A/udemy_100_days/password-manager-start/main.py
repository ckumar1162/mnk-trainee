from tkinter import *
from tkinter import messagebox
import random
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
items = letters + numbers + symbols
#-------------------------------ENCRYPTING PASSWORD-----------------------------#
def encrypt_pw(og_pw,shift_num):
    encoded_pw = ""
    for i in og_pw:
        shift_position = items.index(i) + shift_num
        shift_position %=len(items) 
        encoded_pw += items[shift_position]
    return encoded_pw
        
#---------------------------------Decrypt function---------------------------#
def decrypt_pw(og_pw,shift_num):
    decoded_pw = ""
    for i in og_pw:
        shift_position = items.index(i) - shift_num
        shift_position %=len(items) 
        decoded_pw += items[shift_position]
    return decoded_pw 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbol +password_num

    random.shuffle(password_list)

    password = "".join(password_list)

    pw.insert(END,password)
    pyperclip.copy(password)

   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_input = web.get()
    user_input = user.get()
    password1 = pw.get()
    shift = 2
    if len(website_input) == 0 or len(password1) == 0:
        messagebox.showinfo(title="OOPS!!!",message="Please don't leave any fields empty")
    else:
        encoded = encrypt_pw(password1,shift)
        msg_box = messagebox.askokcancel(title=website_input,message=f'These are the  u have entered:\n email:{user_input}\n password:{password1}\n Is that ok to save? ')
        if msg_box:
            with open(r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\password-manager-start\data.txt",'a') as file:
                file.write(f"{website_input} |{user_input} |{encoded}\n")
                web.delete(0,END)
                pw.delete(0,END)
#-----------------------------login----------------------------#
def login():
    web_input = web.get()
    user_input = user.get()
    password_input = pw.get()
    shift = 2

    if len(web_input) == 0 or len(user_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(message="Please fill the required fields")
        return

    try:
        with open(r'mnk-trainee\\Python\\Mnk-trainee-Vidhya_S_A\\udemy_100_days\\password-manager-start\\data.txt') as data_file:
            content = data_file.readlines()
    except FileNotFoundError:
        messagebox.showerror(message="No such file found")
        return

    for data in content:
        
        saved_website, saved_user, saved_pw = [item.strip() for item in data.strip().split('|')]

        if web_input == saved_website and user_input == saved_user:
            decoded_password = decrypt_pw(saved_pw, shift)
            if password_input == decoded_password:
                messagebox.showinfo(message="Login Successful")
                return
            else:
                messagebox.showerror(message="Invalid password")
                return

    # If no match is found after loop
    messagebox.showerror(message="No matching credentials found!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx = 20,pady = 20)

#creating windows
canvas = Canvas(width=200,height=200)
my_img = PhotoImage(file = r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\password-manager-start\logo.png")
canvas.create_image(100,100,image=my_img)
canvas.grid(column=1,row=0)

#creating labels
website = Label(text="Website:")
website.grid(row=1,column=0)
email = Label(text="Email/Username:")
email.grid(column=0,row=2)
password = Label(text="Password:")
password.grid(column=0,row=3)

#creating entry
web = Entry(width=39)
web.grid(column=1,row =1,columnspan=2 )
web.focus() #the cursor will be highlighted when the app is launched

user = Entry(width=39)
user.grid(column=1,row =2,columnspan=2)
user.insert(END,'vidhya@gmail.com')

pw = Entry(width=21)
pw.grid(column=1,row=3)


#creating buttons
generate = Button(text='Generate password',command=generate_password)
generate.grid(column=2,row= 3)


add = Button(text='Add',width=34,command=save_data)
add.grid(column=1,row= 4,columnspan=2)


login = Button(text='Login',width=34,command=login)
login.grid(column=1,row=5,columnspan=2)




window.mainloop()