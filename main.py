import tkinter
import csv

BACKGROUND_COLOR = "#B1DDC6"
languages = []
index = 0
words = []


def correct_answer():
    global index
    index +=1
    reset()


def reset():
    global index
    canvas.itemconfig(image_on_canvas, image=card_front_img)
    canvas.itemconfig(language, text=main_language)
    canvas.itemconfig(word, text=words[index][0])
    count_down_card()
    count_down_language()
    count_down_word()
    get_data()


def get_data():
    global words
    global index
    with open(".\data\\french_words.csv") as file:
        data = csv.reader(file)
        next(data, None) #to skip headers
        words = [row for row in data]


def count_down_card():
    window.after(3000, change_card)


def count_down_language():
    window.after(3000, change_language)


def count_down_word():
    window.after(3000, change_word)


def change_card():
    canvas.itemconfig(image_on_canvas, image=card_back_img)


def change_language():
    global languages, index
    canvas.itemconfig(language, text=languages[0][1])


def change_word():
    global index
    global words
    canvas.itemconfig(word, text=words[index][1])


def get_languages():
    global languages
    with open(".\data\\french_words.csv") as file:
        data = csv.reader(file)

        for row in data:
            languages.append(row)
            break

#==== GUI =======
window = tkinter.Tk()
window.title("Flash Card App")

get_data()
get_languages()
main_language = languages[index][0]

canvas = tkinter.Canvas(window, width=900, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=2)
card_front_img = tkinter.PhotoImage(file=".\images\card_front.png")
card_back_img = tkinter.PhotoImage(file=".\images\card_back.png")
image_on_canvas = canvas.create_image(450,300,image=card_front_img)
language = canvas.create_text(430, 200, text=main_language, font=("Arial", 50, "italic"))
word = canvas.create_text(430, 350, text=words[index][0], font=("Arial", 70, "italic", "bold"))
canvas.grid(row=0, columnspan=2, column=0)

right_symbol = tkinter.PhotoImage(file=".\images\\right.png")
right_button = tkinter.Button(window, image=right_symbol, highlightthickness=0, command=correct_answer)
right_button.place(x=200, y=570)

wrong_symbol = tkinter.PhotoImage(file=".\images\wrong.png")
wrong_button = tkinter.Button(window, image=wrong_symbol, highlightthickness=0)
wrong_button.place(x=560, y=570)

count_down_card()
count_down_language()
count_down_word()


window.mainloop()
