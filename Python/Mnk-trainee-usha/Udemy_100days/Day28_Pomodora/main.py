from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0 #number sessions you had ,2 reps means 1 work session and 1 break
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    tk.after_cancel(timer)
    #timer_text
    canvas.itemconfig(timer_text,text="00:00")
    #timer_label
    label.config(text="Timer")
    #change checkmarks
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

     # if it is 8th rep
    if reps % 8 == 0:
        count_number(long_break_sec)
        label.config(text="Long Break" ,fg=RED)
    #if it is 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_number(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    # if it is 1st/3rd/5th/7th rep:
    else:
        count_number(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#tkinter has built-in method to every widget
#after - excute a command after a time delay
def count_number(count):
    count_min=math.floor(count / 60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" #dynamic typing-here changing datatype int to str

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=tk.after(1000, count_number, count-1)  # 1sec 1000 ms
    else:
         start_timer()
         marks=""
         work_sessions = math.floor(reps/2)
         for i in range(work_sessions):
             marks+="✔"
         check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

tk=Tk()
tk.title("Pamodora")
tk.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)#those are image length values
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#timer label
label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=("bold",40))
label.grid(column=1,row=0)

#start button
button1=Button(text="Start",highlightthickness=0,command=start_timer)
button1.grid(column=0,row=2)

#reset button
button2=Button(text="Reset",highlightthickness=0,command=reset_timer)
button2.grid(column=2,row=2)

#check mark label
check_mark=Label(fg=GREEN,bg=YELLOW,font=(50))
check_mark.grid(column=1,row=3)

tk.mainloop()
