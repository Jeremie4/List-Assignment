# Import modules
import list_assignment_lib
import customtkinter
import tkinter
import sys


# Set theme
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
customtkinter.set_widget_scaling(1)
customtkinter.set_window_scaling(1)


# Setup window
app = customtkinter.CTk()
app.geometry("1200, 900")
app.minsize(1024, 768)
app.maxsize(2160, 3840)
app.title("List Assignment - Jeremie Marquis")


# Define variables
Electronics = []
Groceries = []
Clothes = []
Books = []
time_ran = 0
x = 0


# Make checkboxes
for i in range(4):
    x += 0.15
    y = 0.05

    for i in range(1,17):
        if time_ran == 0:
            num = i
        elif time_ran == 1:
            num = i + 16
        elif time_ran == 2:
            num = i + 32
        elif time_ran == 3:
            num = i + 48

        y += 0.05
        y = round(y, 2)
        command = ('checkboxtext' + str(num) + ' = ' +  '"item ' + str(num) + '"\ncheckbox' + str(num) + ' = customtkinter.CTkCheckBox(master=app, text=checkboxtext' + str(num) + ')\ncheckbox' + str(num) + '.place(relx=' + str(x) + ', rely=' + str(y) + ', anchor=tkinter.W)')
        exec(command)

    time_ran += 1


# Delete list
def delete_list():
    Groceries.clear()
    Clothes.clear()
    Electronics.clear()
    Books.clear()
    textbox = customtkinter.CTkTextbox(master=app, height=400)
    textbox.insert("0.0", "List deleted")
    textbox.configure(state="disabled")
    textbox.place(relx=0.8, rely=0.45, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="Make List", command=make_list)
    button.place(relx=0.8, rely=0.1, anchor=tkinter.CENTER)


# Make list
def make_list():
    for i in range(1,65):
        num = i
        if num <= 16:
            command = ('if checkbox' + str(num) + '.get() == 1:\n    Groceries.append(checkboxtext' + str(num) + ')')
        elif num <= 32:
            command = ('if checkbox' + str(num) + '.get() == 1:\n    Clothes.append(checkboxtext' + str(num) + ')')
        elif num <= 48:
            command = ('if checkbox' + str(num) + '.get() == 1:\n    Electronics.append(checkboxtext' + str(num) + ')')
        elif num <= 64:
            command = ('if checkbox' + str(num) + '.get() == 1:\n    Books.append(checkboxtext' + str(num) + ')')

        exec(command)

    textbox = customtkinter.CTkTextbox(master=app, height=400)
    textbox.insert("0.0", "Groceries: " + str(Groceries) + "\n")
    textbox.insert("end", "Clothes: " + str(Clothes) + "\n")
    textbox.insert("end", "Electronics: " + str(Electronics) + "\n")
    textbox.insert("end", "Books: " + str(Books) + "\n")
    textbox.configure(state="disabled")
    textbox.place(relx=0.8, rely=0.45, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="Delete List", command=delete_list)
    button.place(relx=0.8, rely=0.1, anchor=tkinter.CENTER)


# Make labels
label_1 = customtkinter.CTkLabel(master=app, text="Groceries", justify=customtkinter.LEFT)
label_1.place(relx=0.2, rely=0.05, anchor=tkinter.CENTER)
label_2 = customtkinter.CTkLabel(master=app, text="Clothes", justify=customtkinter.LEFT)
label_2.place(relx=0.35, rely=0.05, anchor=tkinter.CENTER)
label_3 = customtkinter.CTkLabel(master=app, text="Electronics", justify=customtkinter.LEFT)
label_3.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
label_4 = customtkinter.CTkLabel(master=app, text="Books", justify=customtkinter.LEFT)
label_4.place(relx=0.65, rely=0.05, anchor=tkinter.CENTER)


# Make buttons
button = customtkinter.CTkButton(master=app, text="Make List", command=make_list)
button.place(relx=0.8, rely=0.1, anchor=tkinter.CENTER)
exit_button = customtkinter.CTkButton(master=app, text="Exit", command=sys.exit)
exit_button.place(relx=0.8, rely=0.85, anchor=tkinter.CENTER)
github_button = customtkinter.CTkButton(master=app, text="GitHub", command=list_assignment_lib.open_GitHub_link)
github_button.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)


# Run app
app.mainloop()