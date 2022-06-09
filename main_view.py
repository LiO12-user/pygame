import login_view
from tkinter import *

root = Tk()

def show_button(text, command):
    return Button(root, text=text, command=command)

show_button('login', login_view.run_all_stuf)
show_button('register', )

