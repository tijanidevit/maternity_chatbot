import sqlite3, random, datetime
from models.user import User


def getNewId():
    return random.getrandbits(28)

def insert(user):
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?,?)", (
        getNewId(),
        user['name'],
        user['email'],
        user['password'],
        datetime.datetime.now()
    ))
    conn.commit()
    conn.close()
    return getUser(user['email'])

def view():
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    users = []
    for i in rows:
        user = User(i[0], True if i[1] == 1 else False, i[2], i[3])
        users.append(user)
    conn.close()
    return users

def isEmailExists(email):
    return getUser(email) is not None

def getUser(value):
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=? OR id=?", (value, value))
    user = cur.fetchone()
    conn.close()
    return user

def update(user):
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=?, email=? WHERE id=?", (user.name, user.email, user.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('maternity.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()