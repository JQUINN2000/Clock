from tkinter import *
from time import *

def update():

    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    week_string = strftime('%A')
    week_label.config(text=week_string)

    date_string = strftime('%d/%B/%Y')
    date_label.config(text=date_string)
    window.after(1, update)

window = Tk()

time_label = Label(window,
                   font=('Arial', 50),
                   fg='#00FF00',
                   bg='black')
time_label.pack()

week_label = Label(window,
                   font=('Arial', 50),
                   fg='#00FF00',
                   bg='black')
week_label.pack()

date_label = Label(window,
                   font=('Arial', 50),
                   fg='#00FF00',
                   bg='black')
date_label.pack()

update()

window.mainloop()