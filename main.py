import tkinter
import csv


BACKGROUND_COLOR = "#B1DDC6"
languages = []
index = 0
words = []
timer = None


def correct_answer():
    global index
    update_data()
    reset()


def wrong_answer():
    global index
    index += 1
    reset()


def reset():
    global index
    cancel()
    canvas.itemconfig(image_on_canvas, image=card_front_img)
    canvas.itemconfig(language, text=main_language, fill="black")
    canvas.itemconfig(word, text=words[index][0], fill="black")
    countdown()


def get_data():
    global words, languages
    try:
        with open(".\data\\words_to_learn.csv") as file:
            data = csv.reader(file)
            next(data, None)  # to skip headers
            words = [row for row in data]

    except FileNotFoundError:
        with open(".\data\\french_words.csv") as file:
            data = csv.reader(file)
            next(data, None)  # to skip headers
            words = [row for row in data]

        new_file = open(".\data\\words_to_learn.csv", "w")
        new_file.write(f"{languages[0][0]},{languages[0][1]}\n")
        for row in words:
            new_file.write(f"{row[0]},{row[1]}\n")
        new_file.close()

        with open(".\data\\words_to_learn.csv") as new_file:
            data = csv.reader(new_file)
            next(data, None)  # to skip headers
            words = [row for row in data]


def update_data():
    global index, words
    words.remove(words[index])
    with open(".\data\\words_to_learn.csv", "w") as new_file:
        new_file.write(f"{languages[0][0]},{languages[0][1]}\n")
        for row in words:
            new_file.write(f"{row[0]},{row[1]}\n")


def change_card():
    canvas.itemconfig(image_on_canvas, image=card_back_img)


def change_language():
    global languages, index
    canvas.itemconfig(language, text=languages[0][1], fill="white")


def change_word():
    global index
    global words
    canvas.itemconfig(word, text=words[index][1], fill="white")


def change():
    change_card()
    change_language()
    change_word()


def countdown():
    global timer
    timer = window.after(3000, change)


def cancel():
    global timer
    window.after_cancel(timer)


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

get_languages()
get_data()
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
wrong_button = tkinter.Button(window, image=wrong_symbol, highlightthickness=0, command=wrong_answer)
wrong_button.place(x=560, y=570)

countdown()

window.mainloop()