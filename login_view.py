#main view
import Login as lg

from tkinter import *
import time

root = Tk()

e = Entry(root, width = 50)
e.pack()

e2 = Entry(root, width = 50)
e2.pack()



def store_value():
    name = e.get()
    print(name)
    return name

def store_pass_value():
    password = e2.get()
    print(password)
    return password

def show_label(text, bg):
    label = Label(root, bg = bg, text = text, fg='white')
    label.pack()

user_name = store_value()
user_pass = store_pass_value()

def log():
    if lg.login(store_value(), store_pass_value()):
        show_label('loged successful', 'green')
    else:
        show_label('something went wrong', 'red')


    # root.quit()


my_btn = Button(root, text = "submit name", command=store_value)
my_btn2 = Button(root, text = "submit pass", command=store_pass_value)
my_btn3 = Button(root, text = "login", command=log)

my_btn.pack()
my_btn2.pack()
my_btn3.pack()



root.mainloop()
