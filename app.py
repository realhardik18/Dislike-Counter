from flask import Flask, render_template, request
from threading import Thread
from flask.helpers import url_for

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


def run():
    app.run(host='0.0.0.0')


def show_site():
    t = Thread(target=run)
    t.start()


show_site()
