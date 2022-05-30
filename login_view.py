#main view
import Login as lg

from tkinter import *
import time


#root = Tk()

e.pack()
e2.pack()

user_name = store_value()
user_pass = store_pass_value()

def log():
    if lg.login(store_value(), store_pass_value()):
        show_label('loged successful', 'green')
        return True
    else:
        show_label('something went wrong', 'red')
        return False


    # root.quit()


my_btn = Button(root, text = "submit name", command=store_value)
my_btn2 = Button(root, text = "submit pass", command=store_pass_value)
my_btn3 = Button(root, text = "login", command=log)

my_btn.pack()
my_btn2.pack()
my_btn3.pack()

root.mainloop()


class login_view:
    def __init__(self, root):
        self.root = root
        self.e = Entry(root, width=50)
        self.e2 = Entry(root, width = 50)

    def store_value(self):
        name = self.e.get()
        print(name)
        return name


    def store_pass_value(self):
        password = self.e2.get()
        print(password)
        return password

    def show_label(self, text, bg):
        label = Label(self.root, bg=bg, text=text, fg='white')
        label.pack()


    def show_entry(self):
        self.e.pack()
        self.e2.pack()


