import mysql.connector

# make class
db = db = mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="lukas2007+",
                                  database="game_users_data"
                                  )
mycursor = db.cursor()


def execue_query(self, query):
    self.mycursor.execute(query)


def insert_data(name, password, score, name_hash):
    # self.mycursor.execute(f'insert into user(name, password, score, name_hash) values (%s, %s, %s, %s)", ("{name}", "{password}", {score}, "{name_hash}")')
    q = f"INSERT INTO user(name, password, score, name_hash)" "VALUES ("f"'{name}'"", "f"'{password}'"f", {score}, "f"'{name_hash}'"");"


    mycursor.execute(q)
    db.commit()
    print('data inserted')

    db.rollback()
