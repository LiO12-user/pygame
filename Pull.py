import mysql.connector

# make class
db = db = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="lukas2007+",
                                  database="game_users_data"
                                  )
mycursor = db.cursor()

#def get_name(name):
