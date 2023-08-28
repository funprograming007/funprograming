

# Flask  容易学习的一个 python 建站的包， 使用且仅使用这个包， 目的让大家不要被大量的名词和技术所困扰

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)