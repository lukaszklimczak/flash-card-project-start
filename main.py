import tkinter

BACKGROUND_COLOR = "#B1DDC6"


#==== GUI =======
window = tkinter.Tk()
window.title("Flash Card App")

canvas = tkinter.Canvas(window, width=900, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=2)
card_front_img = tkinter.PhotoImage(file=".\images\card_front.png")
card_back_img = tkinter.PhotoImage(file=".\images\card_back.png")
canvas.create_image(450,300,image=card_front_img)
canvas.grid(row=0, columnspan=2, column=0)

# canvas2 = tkinter.Canvas(width=900, height=100, bg)

right_symbol = tkinter.PhotoImage(file=".\images\\right.png")
right_button = tkinter.Button(window, image=right_symbol)
right_button.place(x=200, y=570)

wrong_symbol = tkinter.PhotoImage(file=".\images\wrong.png")
wrong_button = tkinter.Button(window, image=wrong_symbol)
wrong_button.place(x=560, y=570)

window.mainloop()