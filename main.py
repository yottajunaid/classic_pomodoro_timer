from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#FF9BD2"
RED = "#D63484"
BLACK = "#402B3A"
YELLOW = "#F8F4EC"
FONT_NAME = "Courier"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO TIMER @yottajunaid")
window.config(padx=100, pady=50, bg= YELLOW)

title_label = Label(text= "Timer", fg=BLACK, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column= 0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column= 2, row=2)

check_mark = Label(fg= RED, bg= YELLOW)
check_mark.grid(column= 1, row= 3)







window.mainloop()