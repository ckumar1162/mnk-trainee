import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier",20,'bold')
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)

    canvas.itemconfig(time_set,text='00:00')
    label.config(text='Timer')
    check_box.config(text='')
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    long_sec=LONG_BREAK_MIN * 60
    short_sec=SHORT_BREAK_MIN * 60
    work_sec= WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        label.config(text="Long break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_sec)
        label.config(text='Short break',fg=PINK)
    else:
        count_down(work_sec)
        label.config(text='Work time',fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min=math.floor(count / 60)
    count_sec=count % 60

    if count_sec < 10:
        count_sec=f'0{count_sec}'

    canvas.itemconfig(time_set,text=f'{count_min}:{count_sec}')

    if count >0:
        global timer
        timer = window.after(1000,count_down,count -1)

    else:
        start_timer()
        marks=''
        work_session=math.floor(reps/2)

        for _ in range(work_session):
            marks +='✔'
        check_box.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


canvas=Canvas(width=200,height=224 ,bg=YELLOW , highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)

time_set=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,24,'bold'))
canvas.grid(column=1,row=1)

label=Label(text='Timer',font=FONT_NAME,bg=YELLOW,fg=GREEN )
label.grid(column=1,row=0)

button1=Button(text='start',fg='black',highlightthickness=0 ,command=start_timer)
button1.grid(column=0,row=2)

button2=Button(text='Reset',fg='black',highlightthickness=0 ,command=reset_timer)
button2.grid(column=2,row=2)

check_box=Label(fg=GREEN,bg=YELLOW)
check_box.grid(column=1,row=3)

window.mainloop()
