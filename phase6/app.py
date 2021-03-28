from flask import Flask, render_template ,request,redirect
import sqlite3
app = Flask(__name__)


@app.route('/login.html', methods=['POST', 'GET'])
def login():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        email = request.form['email']
        mail = (email,)
        password = request.form['pass']
        password = (password,)
        email_from_sql = cur.execute('SELECT email FROM Users WHERE email=?', mail)
        email_from_sql = email_from_sql.fetchone()
        password_from_sql = cur.execute('SELECT password FROM Users WHERE password=?', password)
        password_from_sql = password_from_sql.fetchone()
        if email_from_sql and password_from_sql:
            return redirect('/', code=302)
    else:
        return render_template('login.html')


@app.route('/',methods=['POST', 'GET'])
def home():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
         search = request.form['search']
         search = (search,)
         res = cur.execute('SELECT description from Phish_Info WHERE description = ?',search).fetchone()
         request.form['result'] = res
    else:
        return render_template("./index.html")

@app.route('/index.html',methods=['POST', 'GET'])
def index():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        search = request.form['search']
        search = (search,)
        res = cur.execute('SELECT description from Phish_Info WHERE description = ?',search).fetchone()
        request.form['result'] = res
    else:
        return render_template("./index.html")
@app.route('/about.html')
def about():
    return render_template("./about.html")

@app.route('/register.html',methods=['POST', 'GET'])
def reg():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        city = request.form['city']
        name = request.form['name']
        surname = request.form['surname']
        lst = (surname,email,password,city,name,)
        insert_sql = cur.execute('INSERT INTO Users(surename,name,city,email,password) VALUES(?,?,?,?,?)',lst)
        con.commit()
        return redirect('/login.html', code=302)
    else:
        return render_template("./register.html")

@app.route('/services.html')
def services():
    return render_template("./services.html")

if __name__ == "__main__":
    app.run(debug=True)
# con = sqlite3.connect('Proje.db')
# cur = con.cursor()
# email = ('d',)
# password = ('e',)
# email_from_sql = cur.execute('SELECT email FROM Users WHERE email=?', email).fetchone()
# password_from_sql = cur.execute('SELECT password FROM Users WHERE password=?', password).fetchone()
# if email_from_sql and password_from_sql:
#     print("true")
# cur.execute('SELECT email FROM Users WHERE email="d"')
# print(cur.fetchone())
# var = ('a',)
# cur.execute('SELECT email FROM Users WHERE email=?', var)
# print(cur.fetchone())