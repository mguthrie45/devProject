from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def helloName(name=None):
    return render_template('hello.html', name=name)

@app.route('/parks/')
def parks():
    with open('parks.json') as file:
        parks = json.load(file)
    return render_template('parks.html', parks=parks)

if __name__=='__main__':
    app.run()
