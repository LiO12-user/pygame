import  Connector as c

table = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def ask_for_data(s):
    data = input(f'enter your {s}')
    return data

def hash(obj):
    t = []
    o = []
    r = []
    for i in obj:
        t.append(i)

    for u in range(len(obj)):
        o.append(table.index(t[u]))
        print(f'.... {o[u]}')

    for x in range(len(obj)):
        r.append(table[o[x]-1])
        print(r[x])








hash('lukas')





#name = ask_for_data('name')
#password = ask_for_data('password')


#c.insert_data(name, password, 0, 'f')

