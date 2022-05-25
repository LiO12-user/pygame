import mysql.connector
import Registration as regi

db = db = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="lukas2007+",
                                  database="game_users_data"
                                  )
mycursor = db.cursor()

table = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def login(name, password):
    try:
        name = regi.hash(name)
        password = regi.hash(password)

        # user name from db
        mycursor.execute(f"select name_hash from user where password = "f"'{password}'"" ")
        user_name = mycursor.fetchone()
        user_name = ''.join(user_name)

        # user password from db
        mycursor.execute(f"select password from user where name_hash = "f"'{name}'""")
        user_password = mycursor.fetchone()
        user_password = ''.join(user_password)

        if user_name == name and user_password == password:
            print('success')
            return True
    except:
        return False


#login('lukas', "dolinaj")
