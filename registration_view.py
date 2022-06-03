from tkinter import *
import Login as lg

# root
root = Tk()

#e = Entry(root, width=50)
#e.pack()
# root view

def main_loop():
    return root.mainloop()

# view
def entry_1():
    return Entry(root, width=50)

e1 = entry_1()

# view
def entry_2():
    return Entry(root, width=50)

e2 = entry_2()

# show entry 1
def show_entry_1():
    return e1.pack()

# show entry 2
def show_entry_2():
    return e2.pack()

# getting name from entry 1
def get_name():
    print(e1.get())
    return e1.get()

# getting password from entry 2
def get_password():
    print(e2.get())
    return e2.get()

# show green label
def show_green_label():
    return Label(root, bg='green', text='loged successful', fg='white')

# show red label
def show_red_label():
    return Label(root, bg='red', text='something went wrong', fg='white')

# log function

def log():
    if lg.login(e1.get(), e2.get()):
        print(get_name())
        print(get_password())
        show_green_label().pack()
        return True
    else:
        show_red_label()
        return False

# if not working try to create separate buttons without parameters, but working :-)
def show_button(text, command):
    return Button(root, text=text, command=command)


show_entry_1()
show_entry_2()
#get_password()
#get_name()
show_button('submit name', get_name).pack()
show_button('submit password', get_password).pack()
show_button('submit all', log).pack()
print('lol')
print(get_name())
main_loop()

