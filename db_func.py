import sqlite3


def create_db():
    conection = sqlite3.connect('game.db')
    cursor = conection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS User(
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    score INT)
    """)
    conection.commit()
    conection.close()


def add_user(name, score):
    conection = sqlite3.connect('game.db')
    cursor = conection.cursor()
    cursor.execute("INSERT INTO Users (name = ?, score = ?), (name, score)")
    conection.commit()
    conection.close()


def get_stat():
    conection = sqlite3.connect('game.db')
    cursor = conection.cursor()
    cursor.execute("SELECT name, score FROM Users WHERE score > 0")
    users = cursor.fetchall()
    conection.commit()
    conection.close()
    return users
