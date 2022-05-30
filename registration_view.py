from tkinter import *
import Login as lg

# root
root = Tk()


# root view
def main_loop():
    return root.mainloop()

# view
def entry_1():
    return Entry(root, width=50)

# view
def entry_2():
    return Entry(root, width=50)

# show entry 1
def show_entry_1():
    return entry_1().pack()

# show entry 2
def show_entry_2():
    return entry_2().pack()

# getting name from entry 1
def get_name():
    return entry_1().get()

# getting password from entry 2
def get_password():
    return entry_2().get()

# show green label
def show_green_label():
    return Label(root, bg='green', text='loged successful', fg='white')

# show red label
def show_red_label():
    return Label(root, bg='red', text='something went wrong', fg='white')

# log function
def log():
    if lg.login(get_name(), get_password()):
        print(get_name())
        print(get_password())
        show_green_label()
        return True
    else:
        show_red_label()
        return False

# if not working try to create separate buttons without parameters
def show_button(text, command):
    return Button(root, text=text, command=command).pack()

# test function
def print_something():
    print('fkdasjfpdskjfspdfjspdfj')

show_entry_1()
show_entry_2()
#get_password()
#get_name()
show_button('submit name', print_something())
show_button('submit password', print_something())
show_button('submit all', print_something())
main_loop()

