import  Connector as c

table = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def ask_for_data(s):
    data = input(f'enter your {s} pls')
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

    out = "".join(r)
    return out

def encrypt(subj):
    let_arr = []
    pos_arr = []
    fin_arr = []
    word = []

    for i in subj:
        let_arr.append(i)

    for u in range(len(subj)):
        pos_arr.append(table.index(let_arr[u]))
        fin_arr.append(pos_arr[u]+1)
        word.append(table[fin_arr[u]])
        out = "".join(word)

    return out

def register_person():
    name = ask_for_data('name')
    hashed_name = hash(name)

    password = ask_for_data('password')
    hashed_password = hash(password)

    print(f'name is {name}')
    print(f'hashed name is {hashed_name}')
    print(f'hashed pass is {hashed_password}')

    c.insert_data(name, hashed_password, 1, hashed_name)

