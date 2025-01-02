from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
tk=Tk()

current_card={}
x={}
try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    #print(original_data)
    x=original_data.to_dict(orient="records")
else:
    x=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    tk.after_cancel(flip_timer)
    current_card=random.choice(x)
    #print(current_card["French"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_img)
    flip_timer=tk.after(5000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_img)

def is_known():
    x.remove(current_card)
    print(len(x))
    data=pd.DataFrame(x)
    data.to_csv("data/words_to_learn.csv")
    next_card()

tk.title("Flash Card")
tk.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

flip_timer=tk.after(5000,func=flip_card)

canvas=Canvas(width=800,height=526)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=front_img)
card_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",font=("Arial",60,"italic"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_img,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()

tk.mainloop()
