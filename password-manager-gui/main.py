from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


#Does not account for multiple passwords to same website

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
def find_password():


        try:
            with open("Password_manager.json", "r") as file:
                data = json.load(file)
                website=website_entry.get()
                email=data[website]["Email"]
                password=data[website]["Password"]
        except FileNotFoundError:
            messagebox.showerror(title="OOPs",message="Please enter a website into the database")
        except KeyError:
            messagebox.showerror(title="OOPS",message="No data found")
        else:
            messagebox.showinfo(title="Site Found",message=f"The given website has \nEmail: {email}\nPassword: {password}")
def generate_file():
    website_name = website_entry.get()
    Email_name = Email_entry.get()
    password_name = Password_entry.get()

    my_data = {
        website_name: {
            "Email": Email_name,
            "Password": password_name,
        }
    }

    if 0 in [len(website_name), len(Email_name), len(password_name)]:
        messagebox.showerror(title="Error", message="Entry box left empty")
    else:
        try:
            with open(file="Password_manager.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data to new data
                data.update(my_data)
            with open(file="Password_manager.json", mode="w") as file:
                # Write new data
                json.dump(obj=data, fp=file, indent=4)
        except FileNotFoundError:
            with open(file="Password_manager.json", mode="w") as file:
                json.dump(obj=my_data, fp=file, indent=4)
        finally:
            website_entry.delete(0, END)
            Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
logo = PhotoImage(file="logo.png")

window.config(pady=50, padx=50)
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_entry = Entry(width=19)
website_entry.grid(column=1, row=1)
website_entry.focus()



website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

Email_entry = Entry(width=37)
Email_entry.grid(column=1, row=2,columnspan=2)
Email_entry.insert(END, string="SamplaEmail@gmail.com")

Email_label = Label(text="Email/Username")
Email_label.grid(column=0, row=2)

Password_label = Label(text="Password: ")
Password_label.grid(column=0, row=3)

Password_entry = Entry(width=19)
Password_entry.grid(row=3, column=1)

Generate_password_button = Button(text="Generate Password", command=gen_pass)
Generate_password_button.grid(row=3, column=2)

Add = Button(width=30, text="Add", command=generate_file)
Add.grid(row=4, column=1,columnspan=2)

Search_button=Button(width=14,text="Search",command=find_password)
Search_button.grid(column=2,row=1)

window.mainloop()
