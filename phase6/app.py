from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key = "hello"


@app.route('/login.html', methods=['POST', 'GET'])
def login():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        email = request.form['email']
        mail = (email,)
        password = request.form['pass']
        password = (password,)
        email_from_sql = cur.execute(
            'SELECT email FROM Users WHERE email=?', mail)
        email_from_sql = email_from_sql.fetchone()
        password_from_sql = cur.execute(
            'SELECT password FROM Users WHERE password=?', password)
        password_from_sql = password_from_sql.fetchone()
        if email_from_sql and password_from_sql:
            session['user'] = str(email_from_sql)
            return redirect('/', code=302)
    else:
        return render_template('login.html')


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"


@app.route('/', methods=['POST', 'GET'])
def home():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        search = "%" + request.form['search'] + "%"
        search = (search,)
        res = cur.execute(
            "SELECT description, phish2_id from Phish_Info WHERE description LIKE ?", search).fetchone()
        return render_template("./index.html", ans=res)
    else:
        return render_template("./index.html")


@app.route('/index.html', methods=['POST', 'GET'])
def index():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        search = "%" + request.form['search'] + "%"
        search = (search,)
        res = cur.execute(
            "SELECT description, phish2_id from Phish_Info WHERE description LIKE ?", search).fetchone()
        return render_template("./index.html", ans=res)
    else:
        return render_template("./index.html")


@app.route('/about.html')
def about():
    return render_template("./about.html")


@app.route('/register.html', methods=['POST', 'GET'])
def reg():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        city = request.form['city']
        name = request.form['name']
        surname = request.form['surname']
        lst = (surname, email, password, city, name,)
        insert_sql = cur.execute(
            'INSERT INTO Users(surename,name,city,email,password) VALUES(?,?,?,?,?)', lst)
        con.commit()
        return redirect('/login.html', code=302)
    else:
        return render_template("./register.html")


@app.route('/services.html')
def services():
    return render_template("./services.html")


if __name__ == "__main__":
    app.run(debug=True)
