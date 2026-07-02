from tkinter import *

# ---------------------------- FUNCTION ------------------------------- #
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.60934
    no_of_km.config(text=f"{km:.2f}")


# ---------------------------- WINDOW ------------------------------- #
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# ---------------------------- ENTRY ------------------------------- #
miles_input = Entry(window, width=15)
miles_input.insert(END, "0")
miles_input.grid(row=0, column=1)

# ---------------------------- LABELS ------------------------------- #
miles_label = Label(window, text="Miles", font=("Arial", 20))
miles_label.grid(row=0, column=2)
miles_label.config(padx=20, pady=20)

is_equal_to_label = Label(window, text="Is equal to", font=("Arial", 20))
is_equal_to_label.grid(row=1, column=0)
is_equal_to_label.config(padx=20, pady=20)

no_of_km = Label(window, text="0", font=("Arial", 20))
no_of_km.grid(row=1, column=1)
no_of_km.config(padx=20, pady=20)

km_label = Label(window, text="Km", font=("Arial", 20))
km_label.grid(row=1, column=2)
km_label.config(padx=20, pady=20)

# ---------------------------- BUTTON ------------------------------- #
button = Button(window, text="Calculate", width=10, command=calculate)
button.grid(row=2, column=1)
button.config(padx=10, pady=10)

window.mainloop()