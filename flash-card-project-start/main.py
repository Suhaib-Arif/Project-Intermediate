from tkinter import *
import pandas
from random import choice


try:
    word = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = word.to_dict(orient="records")
    questions = choice(to_learn)


def display_english():
    Title.config(text="English", bg=BACKGROUND_COLOR)

    Word.config(text=questions["English"], bg=BACKGROUND_COLOR)
    canvas.itemconfig(card, image=tablet2)


def display_french():
    global questions
    global after_timer
    Title.config(text="French", bg=White)
    questions = choice(to_learn)
    canvas.itemconfig(card, image=tablet1)
    window.after_cancel(after_timer)
    Word.config(text=questions["French"], bg=White)
    after_timer = window.after(3000, display_english)

    # print(to_learn)


def remove_question():
    global questions
    to_learn.remove(questions)
    display_french()
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv")


BACKGROUND_COLOR = "#B1DDC6"
White = "#fff"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

tablet1 = PhotoImage(file="images/card_front.png")
tablet2 = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card = canvas.create_image(400, 256, image=tablet1)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

X = PhotoImage(file="images/wrong.png")
X_button = Button(image=X, highlightthickness=0, command=display_french)
X_button.grid(column=0, row=1)

Tick = PhotoImage(file="images/right.png")
Tick_button = Button(image=Tick, highlightthickness=0, command=remove_question)
Tick_button.grid(column=1, row=1)

Title = Label(text="Title", font=("Ariel", 40, "italic"), bg=White)
Title.place(x=280, y=130)

Word = Label(text="Word", font=("Ariel", 60, "bold"), bg=White)
Word.place(x=260, y=230)

after_timer = window.after(3000, display_english)
display_french()

window.mainloop()
