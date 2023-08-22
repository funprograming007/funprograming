
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

app.run(host='0.0.0.0')
