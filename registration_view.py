from tkinter import *
import Registration as r
import Login as lg

# root
#root = Tk()

def main_loop(root):
    return root.mainloop()


# prve pole do ktoreho sa zadava meno
def entry_1(root):
    return Entry(root, width=50)


e1 = entry_1()


# druhe pole do ktoreho sa zadava heslo
def entry_2(root):
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
def show_green_label(root):
    return Label(root, bg='green', text='loged successful', fg='white')


# show red label
def show_red_label(root):
    return Label(root, bg='red', text='something went wrong', fg='white')

# register function
def register(root):
    try:
        r.register_person(get_name(), get_password())
        show_green_label(root)
    except:
        show_red_label(root)


def show_button(text, command, root):
    return Button(root, text=text, command=command)


def run_all_stuff(root):
    e1 = entry_1()

    show_entry_1()
    show_entry_2()
    show_button('submit all', register, root).pack()
    main_loop(root)


