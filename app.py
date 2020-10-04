from flask import Flask, request, redirect, url_for, render_template
import json

app = Flask(__name__)

@app.route('/')
def helloWorld(info=None):
    return render_template('login.html', return_info=info)

@app.route('/login/', methods=['POST', 'GET'])
def login_form():
    users = {"devpsu": 'devpsu'} #username: password


    username = request.form.get('username', False)
    password = request.form.get('password', False)
    print(username, password)

    first_time = username is False or password is False

    if not first_time:
        if username not in users:
            return render_template('login.html', return_info='Username not found')
        elif users[username] != password:
            return render_template('login.html', return_info='Incorrect password')
        else:
            return redirect(url_for('parks'))
    else:
        return render_template('login.html')

@app.route('/parks/')
def parks():
    with open('parks.json') as file:
        parks = json.load(file)
    return render_template('parks.html', parks=parks)

if __name__=='__main__':
    app.run(debug=False)
