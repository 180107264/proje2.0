import sqlite3
con = sqlite3.connect('Proje.db')
cur = con.cursor()
email = 'd'
email = (email,)
password = ('e',)
email_from_sql = cur.execute('SELECT email FROM Users WHERE email=?', email).fetchone()
password_from_sql = cur.execute('SELECT password FROM Users WHERE password=?', password).fetchone()
if email_from_sql and password_from_sql:
    print("true")