from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website)<=0 or len(password)<=0 or len(email)<=0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail:{email} \nPassword: {password}"
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width= 200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo)
canvas.grid(column=1 ,row=0)

def labels(text, x, y):
    my_label = Label(text=text)
    my_label.grid(column=x ,row=y)

labels("Website:", 0, 1)
labels("Email/Username:", 0, 2)
labels("Password:", 0, 3)

website_input = Entry(width=51)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "mparts578@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3, columnspan=1)

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column= 2, row= 3)

pass_add_button = Button(width=44, text="Add", command=save)
pass_add_button.grid(column= 1, row= 4, columnspan= 2)

window.mainloop()
