from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
filepath = r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\data\German_Basic_Words.csv'
current_card={}
new_data = {}
#---------------------------------Functions for button-------------------------------------------#
try:
    data = pd.read_csv(r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\data\words_to_learn.csv',encoding="latin1")
except FileNotFoundError:
    og_data = pd.read_csv(filepath,encoding='latin1')
    new_data = og_data.to_dict(orient='records') 
else:       
    new_data = data.to_dict(orient='records') #orient = records provide as key value pairs,if we directly use to_dict it will produce a list that startswith all the keys and then shows the value


def next_button():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(new_data)
    canvas.itemconfig(title,text='German',fill='black')
    canvas.itemconfig(word,text=current_card['German'],fill='black')
    canvas.itemconfig(card,image=my_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(title,text='English',fill='white')
    canvas.itemconfig(word,text=current_card['English'],fill='white')
    canvas.itemconfig(card,image=back_img)

def is_known():
    new_data.remove(current_card)
    print(len(new_data))
    data = pd.DataFrame(new_data)
    data.to_csv(r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\data\words_to_learn.csv',index = False)
    next_button()

#-----------------------------------UI setup----------------------------------#
window = Tk()
window.title('Flash card')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
my_img = PhotoImage(file=r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\images\card_front.png')
back_img = PhotoImage(file=r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\images\card_back.png')
card = canvas.create_image(400,263,image=my_img)
title = canvas.create_text(400,120,text='',font=('arial',30,'bold'))
word = canvas.create_text(400,263,text='',font=('arial',50,'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)


#creating buttons
right_button = PhotoImage(file=r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\images\right.png')
button1 = Button(image=right_button,highlightthickness=0,command=is_known)
button1.grid(column=0,row=1)

next = PhotoImage(file=r'mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\flash-card-project-start\images\next-button-icon-png-32.png')
button2 = Button(image=next,highlightthickness=0,command=next_button)
button2.grid(column=1,row=1)

















next_button()

window.mainloop()
