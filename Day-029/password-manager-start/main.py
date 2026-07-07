from tkinter import *
from tkinter import messagebox
from pathlib import Path
import os
from random import choice, randint, shuffle
import json

BASE_DIR = Path(__file__).parent
base_dir = os.path.dirname(os.path.abspath(__file__))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  password_list = []
  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = password_letters + password_numbers + password_symbols
  shuffle(password_list)

  password = "".join(password_list)
  password_input.insert(0, password)
#   print(f"Your password is: {password}")

# ----------------------------FIND PASSWORD------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open(os.path.join(base_dir, "Saved_Users.json"), "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showerror(title="error", message="No data File Found!. ")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Website", message=f"Email: {email}\n Password{password}")
            else:
                 messagebox.showerror(title="Error", message=f"There are NO details for{website} exits!.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().strip().capitalize()
    email = email_input.get().strip()
    password = password_input.get().strip()
    new_data = {
         website:  {
              "email": email,
              "password": password,        
        }
    }
    if not website or not email or not password:
            messagebox.showerror(title="Oops", message="Please dont leave any fields empty!")


    else:
        try:
            with open(os.path.join(base_dir, "Saved_Users.json"), "r") as data_file:
                #Reading old data

                data = json.load(data_file)

        except FileNotFoundError:

            with open(os.path.join(base_dir, "Saved_Users.json"), "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
                
             #Updating old data
            data.update(new_data)


            with open(os.path.join(base_dir, "Saved_Users.json"), "w") as data_file:


                #Saving updated data
                json.dump(data, data_file, indent=4)
        
        finally:
        
            website_input.delete(0, END)
            password_input.delete(0, END)
               
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady= 20)


canvas = Canvas(width=200, height=200)
Logo = PhotoImage(
    file=str(BASE_DIR / "logo.png"))
canvas.create_image(100, 100, image=Logo)
canvas.grid(row=0, column=1)

website_text = Label(text = "Website:")
website_text.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)

search_button = Button(text="search", width=13, command=find_password)
search_button.grid(row=1, column=2)


email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.insert(0, "sadiqnagoda1848@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

 

Password_text = Label(text="Password:")
Password_text.grid(row=3, column=0, )
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

Password_generator = Button(text="Generate Password", command=generate_password)
Password_generator.grid(row=3, column=2)

add_input = Button(text="add", width=36, command=save)

add_input.grid(row=4, column=1, columnspan=2)



















window.mainloop()