from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window  = Tk()
window.title("My First GUI prgram")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label= Label(text="My First GUI Program", font=("Ariel", 24, ))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

#Button
button = Button(text="Click me", command = button_clicked)
button.grid(row=1, column=1)

button = Button(text="Click me", command = button_clicked)
button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(row=2, column=3)




window.mainloop()