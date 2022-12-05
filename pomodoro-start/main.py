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
reps = 0
tick=""
loop=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global tick
    global reps
    window.after_cancel(id=loop)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer",fg=GREEN)
    tick=""
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    global tick

    long_work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        counter(long_work_seconds)
        label.config(text="Work",fg=RED)
        tick+="✓"
        Tick.config(text=tick)
    elif reps == 7:
        counter(long_break_seconds)
        label.config(text="Break",fg=PINK)
    else:
        counter(short_break_seconds)
        label.config(text="Break",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def counter(count):
    global reps
    global loop
    count_sec = math.floor(count % 60)
    if count_sec <= 9:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{math.floor(count / 60)}:{count_sec}")
    if count > 0:
        loop=window.after(1000, counter, count - 1)
    else:
        reps += 1
        timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORA")
# window.geometry("750x350")
window.config(padx=50, pady=50, bg=YELLOW)

# window.after(1000,my_funt,7)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="C:/Users/Imad/Downloads/pomodoro-start/tomato.png")
canvas.create_image(100, 100, image=photo)
timer_text = canvas.create_text(100, 115, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
label.grid(row=0, column=1)
# label.config(height=10,width=10)

button = Button(text="Start", command=timer)
button.grid(row=2, column=0)

button2 = Button(text="Reset",command=reset_timer)
button2.grid(row=2, column=2)

Tick = Label(fg=GREEN, bg=YELLOW)
Tick.grid(row=3, column=1)

window.mainloop()
