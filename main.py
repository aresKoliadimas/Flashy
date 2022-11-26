from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_list = data.to_dict(orient="records")

rand_word = {}


def next_word():
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    rand_word = random.choice(data_list)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=rand_word['French'], fill="black")
    canvas.itemconfig(image, image=front_card_img)
    flip_timer = window.after(3000, show_trans)


def word_known():
    data_list.remove(rand_word)
    df = pandas.DataFrame(data_list)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_word()

def show_trans():
    canvas.itemconfig(image, image=back_card_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=rand_word['English'], fill="white")


# create the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_trans)

# create the card
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0)
image = canvas.create_image(400, 263, image=front_card_img)
language = canvas.create_text(400, 150, text="", font=LANG_FONT)
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

# create the buttons
x_image = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_word)
x_button.grid(column=0, row=1)

v_image = PhotoImage(file="images/right.png")
v_button = Button(image=v_image, highlightthickness=0, command=word_known)
v_button.grid(column=1, row=1)

next_word()


window.mainloop()
