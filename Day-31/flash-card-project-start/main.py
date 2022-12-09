import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

card = {}
french_dict = {}


def generate_random_word():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(french_dict)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_img)


def is_known():
    french_dict.remove(card)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random_word()


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

try:
    french_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    french_dict = original_words.to_dict(orient="records")
else:
    french_dict = french_words.to_dict(orient="records")

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=generate_random_word)
unknown_button.grid(row=1, column=0)

check_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

window.mainloop()
