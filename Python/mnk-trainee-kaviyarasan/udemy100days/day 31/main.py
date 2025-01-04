from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    to_learn = pd.read_csv("data/french_words.csv").to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    update_card("French", current_card["French"], card_front_img, "black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    update_card("English", current_card["English"], card_back_img, "white")

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

def update_card(title, word, img, color):
    canvas.itemconfig(card_title, text=title, fill=color)
    canvas.itemconfig(card_word, text=word, fill=color)
    canvas.itemconfig(card_background, image=img)

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
Button(image=wrong_img, highlightthickness=0, command=next_card).grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
Button(image=right_img, highlightthickness=0, command=is_known).grid(row=1, column=1)

next_card()
window.mainloop()
