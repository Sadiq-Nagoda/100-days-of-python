from tkinter import *
from pathlib import Path
import pandas as pd
import random

BASE_DIR = Path(__file__).resolve().parent
# base_dir = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

if (BASE_DIR/ "words_to_learn").exists():
    file_path = BASE_DIR/"words_to_learn"
else:
    file_path = BASE_DIR / "data" / "french_words.csv"

DataFrame = pd.read_csv(file_path)
Words = DataFrame.to_dict(orient="records")


flip_timer = None

def print_words():
    global current_card, flip_timer

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(Words)

    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(3000, flip_card)
    Words.remove(current_card)
    df = pd.DataFrame(Words)
    df.to_csv("words_to_learn.csv", index=False)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_word, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])


    


canvas =  Canvas(width=800, height=526)

card_front_image = PhotoImage(
    file=str(BASE_DIR / "images/card_front.png"))                                                           
canvas.create_image(400, 263, image=card_front_image)

card_back_image = PhotoImage(
    file=str(BASE_DIR / "images/card_back.png"))                                                           
canvas_image = canvas.create_image(400, 263, image=card_back_image)


card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(
    file=str(BASE_DIR / "images/wrong.png")) 

Unknown_butotn = Button(image=cross_image, highlightthickness=0)
Unknown_butotn.grid(row=1, column=0)

cherkmark = PhotoImage(
    file=str(BASE_DIR / "images/right.png")) 

known_butotn = Button(image=cherkmark, highlightthickness=0, command=print_words)
known_butotn.grid(row=1, column=1)


window.mainloop()
