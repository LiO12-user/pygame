import mysql.connector

db = db = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="lukas2007+",
                                  database="game_users_data"
                                  )
mycursor = db.cursor()

table = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def login_hash(obj):
    t = []
    o = []
    r = []
    for i in obj:
        t.append(i)

    for u in range(len(obj)):
        o.append(table.index(t[u]))
        print(f'.... {o[u]}')

    for x in range(len(obj)):
        r.append(table[o[x] - 1])
        print(r[x])

    out = "".join(r)
    return out


def login(name, password):
    name = login_hash(name)
    password = login_hash(password)

    # user name from db
    mycursor.execute(f"select name_hash from user where password = "f"'{password}'"" ")
    user_name = mycursor.fetchone()

    # user password from db
    mycursor.execute(f"select password from user where name_hash = "f"'{name}'""")
    user_password = mycursor.fetchone()

    if name == user_name and user_password == password:
        print('loged succesful')
    else:
        print('not')





login('lukas', "dolinaj")
