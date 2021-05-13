from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key = 'secret'
    
            

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
            user_id = cur.execute(
                "SELECT user_id FROM Users WHERE email=?", mail).fetchall()
            session['user'] = cur.execute(
                "SELECT name FROM Users WHERE email=?", mail).fetchall()
            session['id'] = user_id
            return redirect('/', code=302)
        else:
            return render_template('login.html', error="Mail or password was wrong",)
    else:
        return render_template('login.html', )

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
        lst = (name, surname, city, email, password,)
        insert_sql = cur.execute(
            'INSERT INTO Users(name,surname,city,email,password) VALUES(?,?,?,?,?)', lst)
        con.commit()
        return redirect('/login.html', code=302)
    else:
        return render_template("./register.html")

@app.route('/account.html', methods=['POST', 'GET'])
def account():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == "POST":
        res = cur.execute(
            "SELECT domain, description from Phish2 WHERE user_id = ?", session['id'][0]).fetchall()
        domain = request.form['domain']
        desc = request.form['desc']
        user_id = session['id'][0][0]
        lst = (domain, desc, user_id,)
        insert_sql = cur.execute(
            'INSERT INTO Phish2(domain,description,user_id) VALUES(?,?,?)', lst)
        con.commit()
        return  render_template("./account.html", user=session['user'][0][0], ans=res)
    else:
        try:
            res = cur.execute(
            "SELECT domain, description from Phish2 WHERE user_id = ?", session['id'][0]).fetchall()
            return render_template("./account.html", user=session['user'][0][0], ans=res)
        except:
            return redirect('/login.html', code=302)


@app.route('/search_by_user.html', methods=['POST', 'GET'])
def search_by_user():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == "POST":
        search = request.form['name']
        search = (search,)
        user_id = cur.execute(
            "SELECT user_id FROM Users WHERE name=?", search).fetchall()[0][0]
        user_id = (user_id,)
        res = cur.execute(
            "SELECT domain, description from Phish2 WHERE user_id = ?", user_id).fetchall()
        return render_template("search_by_user.html", ans=res )
    else:
        return render_template("search_by_user.html")


@app.route('/types_of_phish.html', methods=['POST', 'GET'])
def types():
    con = sqlite3.connect('Proje.db')
    cur = con.cursor()
    if request.method == "POST":
        search = request.form['types']
        search = (search,)
        res = cur.execute(
            "SELECT domain, description from Phish1 WHERE types = ?", search).fetchone()
        return render_template("types_of_phish.html", ans=res)
    else:
        return render_template("types_of_phish.html", )


@app.route('/user')
def user():
    user_id = session['id'][0]
    return f'<h1>{user_id}</h1>'


@app.route('/logout')
def logout():
    try:
        session.pop('user', None)
        session.pop('id', None)
        return redirect('/', code=302)
    except:
        return redirect('/', code=302)


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
        try:
            return render_template("./index.html", user_id=session['id'])
        except:
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
        try:
            return render_template("./index.html", user_id=session['id'])
        except:
            return render_template("./index.html")


@app.route('/about.html')
def about():
    return render_template("./about.html")

@app.route('/services.html')
def services():
    return render_template("./services.html")


if __name__ == "__main__":
    app.run(debug=True)
