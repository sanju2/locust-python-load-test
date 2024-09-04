from flask import Flask, request
from random import randint
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return 'ok'

@app.route('/about')
def about():
    return 'ok'

@app.route('/random')
def random():
    sleep(randint(0,2))
    return 'ok'

@app.route("/item")
def items():
    item_id = request.args.get("id",None)
    return f"OK - {item_id}"

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "post":
        return "OK_POST"
    else:
        return "OK_GET"

if __name__ == '__main__':
    app.run()