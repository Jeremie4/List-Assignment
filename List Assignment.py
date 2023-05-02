import tkinter
import customtkinter
import sys
import webbrowser

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
customtkinter.set_widget_scaling(1)  # widget dimensions and text size
customtkinter.set_window_scaling(1)  # window geometry dimensions

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1200, 900")
app.minsize(1200, 900)
app.maxsize(2160, 3840)
app.title("List Assignment - Jeremie Marquis")

shopping_list = []
x = 0
time_ran = 0


for i in range(6):
    x += 0.1
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
        elif time_ran == 4:
            num = i + 64
        elif time_ran == 5:
            num = i + 80
        y += 0.05
        y = round(y, 2)
        command = ('checkboxtext' + str(num) + ' = ' +  '"item ' + str(num) + '"\ncheckbox' + str(num) + ' = customtkinter.CTkCheckBox(master=app, text=checkboxtext' + str(num) + ')\ncheckbox' + str(num) + '.place(relx=' + str(x) + ', rely=' + str(y) + ', anchor=tkinter.W)')
        exec(command)
    time_ran += 1


def cancel_order():
    textbox = customtkinter.CTkTextbox(master=app)
    textbox.insert("0.0", "Order Canceled")
    textbox.configure(state="disabled")
    textbox.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="Place Order", command=place_order)
    button.place(relx=0.8, rely=0.1, anchor=tkinter.CENTER)


def place_order():
    for i in range(1,97):
        num = i
        command = ('if checkbox' + str(num) + '.get() == 1:\n    shopping_list.append(checkboxtext' + str(num) + ')')
        exec(command)

    
    textbox = customtkinter.CTkTextbox(master=app)
    textbox.delete("0.0", "end")
    textbox.insert("0.0", shopping_list)
    textbox.configure(state="disabled")
    textbox.place(relx=0.8, rely=0.3, anchor=tkinter.CENTER)
    #label = customtkinter.CTkLabel(master=app, text=(shopping_list), justify=customtkinter.LEFT)
    #label.place(relx=0.8, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="Cancel Order", command=cancel_order)
    button.place(relx=0.8, rely=0.1, anchor=tkinter.CENTER)

def open_link():
    webbrowser.open('https://github.com/Jeremie4/Menu-Project')

button = customtkinter.CTkButton(master=app, text="Place Order", command=place_order)
button.place(relx=0.8, rely=0.1, anchor=tkinter.CENTER)
exit_button = customtkinter.CTkButton(master=app, text="Exit", command=(sys.exit))
exit_button.place(relx=0.8, rely=0.85, anchor=tkinter.CENTER)
github_button = customtkinter.CTkButton(master=app, text="GitHub", command=open_link)
github_button.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)


app.mainloop()