import sqlite3, random


def getNewId():
    return random.getrandbits(28)


def connect():
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()
