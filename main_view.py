from login_view import run_all_stuf
from registration_view import run_all_stuff
from tkinter import *

root = Tk()

print('lolol')

def show_button(text, command):
    return Button(root, text=text, command=command)

show_button('login', run_all_stuf).pack()
show_button('register', run_all_stuff).pack()

root.mainloop()
root.destroy()

