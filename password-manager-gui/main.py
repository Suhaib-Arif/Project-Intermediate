from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    Password_entry.insert(index=0, string="".join(password_list))

    pyperclip.copy("".join(password_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def generate_file():
    website_name = website_entry.get()
    Email_name = Email_entry.get()
    password_name = Password_entry.get()

    if 0 in [len(website_name), len(Email_name), len(password_name)]:
        messagebox.showerror(title="Error", message="Entry box left empty")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"The following are the details \nEmail: {Email_name}\nPassword: {password_name}")
        if is_ok:
            with open(file="Password_manager.txt", mode="a") as file:
                file.write(f"{website_name} | {Email_name} |{password_name} \n")
            website_entry.delete(0, END)
            Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
logo = PhotoImage(file="logo.png")

window.config(pady=50, padx=50)
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=3)
website_entry.focus()

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

Email_entry = Entry(width=36)
Email_entry.grid(column=1, row=2, columnspan=3)
Email_entry.insert(END, string="SamplaEmail@gmail.com")

Email_label = Label(text="Email/Username")
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3)

Password_entry = Entry(width=18)
Password_entry.grid(row=3, column=1)

Generate_password_button = Button(text="Generate Password", command=gen_pass)
Generate_password_button.grid(row=3, column=2)

Add = Button(width=30, text="Add", command=generate_file)
Add.grid(row=4, column=1, columnspan=3)

window.mainloop()
