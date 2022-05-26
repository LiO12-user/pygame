# main view


from tkinter import *
import time

root = Tk()

# spustanie classov funkciami

my_btn = Button(root, text="register", command=registration_view)
my_btn2 = Button(root, text="login", command=login_view)

my_btn.pack()
my_btn2.pack()

root.mainloop()
