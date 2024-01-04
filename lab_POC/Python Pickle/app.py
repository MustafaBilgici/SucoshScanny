from functools import wraps
from flask import Flask, render_template, url_for, request, session, redirect, make_response
import pickle
import sqlite3
import base64


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


def create_app():
    app = Flask(__name__)
    app.secret_key = "fcaa3de2510840af999a7aec3b4bf178"
    with app.app_context():
        init_db()

    return app


def logged_in(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get("loggedIn"):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated_func


def get_user(username):
    query = "SELECT username, password from users where username=:username"
    conn = sqlite3.connect("db/cyberpathpickle.db")
    cursor = conn.cursor()
    user = cursor.execute(query, {'username': username}).fetchall()
    conn.commit()
    conn.close()
    return user


def init_db():
    users = [('admin', 'admin'), ('default', 'default')]
    conn = sqlite3.connect("db/cyberpathpickle.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username CHAR, password CHAR)")
    total = cursor.execute("SELECT count(*) from users").fetchone()

    conn.commit()
    if(total[0] == 0):
        cursor.executemany(
            "INSERT INTO users (username, password) VALUES (?, ?)", users)
        conn.commit()


app = create_app()


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'remember_me' in request.cookies:
        b64 = request.cookies.get("remember_me")
        dump = pickle.loads(base64.urlsafe_b64decode(b64))
        session['username'] = dump.username
        session['loggedIn'] = True
        return redirect(url_for('dashboard'))

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        remember_me = request.form.get("remember_me")
        user = get_user(username)
        if user:
            if user[0][1] == password:
                session['username'] = user[0][0]
                session['loggedIn'] = True
                user_class = User(user[0][0], user[0][1])
                if remember_me:
                    if remember_me == 'on':
                        dump = pickle.dumps(user_class)
                        b64 = base64.b64encode(dump)
                        resp = make_response(redirect(url_for('dashboard')))
                        resp.set_cookie("remember_me", b64)
                        return resp
                else:
                    return redirect(url_for('dashboard'))

    return render_template("index.html")


@app.route('/dashboard')
@logged_in
def dashboard():
    return render_template("dashboard.html", username=session['username'])


@app.route('/logout')
@logged_in
def logout():
    session.clear()
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('remember_me', '', expires=0)
    return resp


@app.errorhandler(404)
def page_not_found(e):
    return "404 not found"


if __name__ == "__main__":
    app.run("0.0.0.0", port=3200, debug=True)
