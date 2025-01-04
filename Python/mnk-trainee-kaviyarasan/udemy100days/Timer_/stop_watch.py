from tkinter import *
import time

running = False
timer = None
seconds = 0
start_time = 0

def count_up():
    global seconds, timer, start_time
    if running:
        elapsed_time = time.time() - start_time
        seconds = int(elapsed_time * 100)
        minutes = seconds // 6000
        secs = (seconds // 100) % 60
        centiseconds = seconds % 100
        canvas.itemconfig(timer_text, text=f"{minutes:02}:{secs:02}.{centiseconds:02}")
        timer = window.after(10, count_up)

def start_timer():
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - seconds / 100
        count_up()

def stop_timer():
    global running
    running = False

def reset_timer():
    global running, seconds
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00.00")
    running = False
    seconds = 0

window = Tk()
window.title("Stopwatch")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224, highlightthickness=0)
timer_text = canvas.create_text(80, 112, text="00:00.00", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text="Stop", highlightthickness=0, command=stop_timer)
stop_button.grid(column=1, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
