from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#C2FFC7"
YELLOW = "#1F4529"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
cycle = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer,text = "00:00")
    title.config(text="Timer")
    completed.config(text="")
    global cycle
    cycle = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global cycle
    cycle += 1

    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    l_break_sec = LONG_BREAK_MIN * 60

    if cycle % 8 == 0:
        count_down(l_break_sec)
        title.config(text='Long Time',fg=RED,bg = GREEN,font=(FONT_NAME,45,'bold'))
    elif cycle % 2 == 0:
        count_down(s_break_sec)
        title.config(text=' Short Break ',fg=PINK,bg = GREEN,font=(FONT_NAME,45,'bold'))
    else:
        count_down(work_sec)
        title.config(text='Work Time',fg=YELLOW,bg = GREEN,font=(FONT_NAME,45,'bold'))        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec =f"0{sec}"
    canvas.itemconfig(text_timer,text=f'{min}:{sec}')
    if count > 0:
        global timer
        timer = canvas.after(1000,count_down,count - 1)
    else:
        start_timer() 
        mark = ""
        work_session = math.floor(cycle/2)
        for _ in range(work_session):
            mark += '👍'  
        completed.config(text = mark) 
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=GREEN)

#creating labels
title = Label(text='Timer',fg=YELLOW,bg = GREEN,font=(FONT_NAME,45,'bold'))
title.grid(column=1,row=0)

#creating canvas
canvas = Canvas(width=300,height=300,bg=GREEN,highlightthickness=0)
timer_img = PhotoImage(file = r"mnk-trainee\Python\Mnk-trainee-Vidhya_S_A\udemy_100_days\pomodoro-start\timer-min.png")
canvas.create_image(150,150,image = timer_img)
text_timer = canvas.create_text(150,150,text="00:00",font=(FONT_NAME,45,'bold'))
canvas.grid(column=1,row=1)

#creating buttons
start = Button(text='Start',highlightthickness=0,width=8,height=2,font=(FONT_NAME,14),command=start_timer)
start.grid(column=0,row=3)
reset = Button(text='Reset',highlightthickness=0,width=8,height=2,font=(FONT_NAME,14),command=reset_timer)
reset.grid(column=3,row=3)

completed = Label(fg="black",bg = GREEN,font =(50))
completed.grid(column=1,row=3)








window.mainloop()