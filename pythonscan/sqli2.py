from flask import Flask, request
import re

app = Flask(__name__)

def check_sql_injection_vulnerability(code):
    select_pattern = re.compile(r"SELECT\s.+?\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")
    insert_pattern = re.compile(r"INSERT\sINTO\s.+?\sVALUES\s?\(.+?\)")
    update_pattern = re.compile(r"UPDATE\s.+?\sSET\s.+\s=\s.+\sWHERE\s.+\s=\s.+\s")
    delete_pattern = re.compile(r"DELETE\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")

    matches = select_pattern.findall(code) + insert_pattern.findall(code) + update_pattern.findall(code) + delete_pattern.findall(code)

    for match in matches:
        if request.method == 'POST':
            if request.form and any(substring in match for substring in request.form):
                print("Potential SQL injection vulnerability detected in POST request: " + match)
        elif request.method == 'GET':
            if request.args and any(substring in match for substring in request.args):
                print("Potential SQL injection vulnerability detected in GET request: " + match)

    if not matches:
        print("No SQL injection vulnerabilities detected.")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # SQL sorgusu
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)

        # ...

    return '''
        <form method="post">
            <input type="text" name="username" />
            <input type="password" name="password" />
            <input type="submit" value="Login" />
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
