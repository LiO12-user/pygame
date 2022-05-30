from tkinter import *
import Login as lg

def is_loged():
    pass


class login_view:
    def __init__(self, root):
        self.root = root
        self.e = Entry(root, width=50)
        self.e2 = Entry(root, width=50)

    def store_value(self):
        name = self.e.get()
        print(name)
        return (name)

    def store_pass_value(self):
        password = self.e2.get()
        print(password)
        return str(password)

    def show_label(self):
        label = Label(self.root, bg='green', text='loged successful', fg='white')
        label.pack()

    def show_label_wrong(self):
        label = Label(self.root, bg='red', text='something went wrong', fg='white')
        label.pack()

    def show_entry(self):
        self.e.pack()
        self.e2.pack()

    def log(self, show_green_label, show_label_wrong, name_func, pass_func):
        if lg.login(name_func, pass_func):
            #show_green_label()
            return True
        else:
            #show_label_wrong()
            return False

    def show_all(self):
        self.root.mainloop()

    def show_btns(self, func1, func2, func3):
        my_btn1 = Button(self.root, text="submit name", command=func1)
        my_btn2 = Button(self.root, text="submit password", command=func2)
        my_btn3 = Button(self.root, text="submit all", command=func3)
        my_btn1.pack()
        my_btn2.pack()
        my_btn3.pack()

v = login_view(Tk())
v.show_entry()
# dorobit show label

name = v.store_value()

show_lbl = v.show_label()
show_red_lbl = v.show_label_wrong()

def show_label():
    label = Label(v.root, bg='green', text='loged succesful', fg='white')
    label.pack()


def show_label_wrong():
    label = Label(v.root, bg='red', text='something went wrong', fg='white')
    label.pack()

v.show_btns(v.store_value(), v.store_pass_value(), v.log(show_lbl, show_red_lbl, v.store_value(), v.store_pass_value()))
#v.show_btns(v.store_value(), v.store_pass_value(), v.log)
v.show_all()