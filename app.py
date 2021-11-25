from flask import Flask, render_template, request
from threading import Thread
from flask.helpers import url_for
from counter import return_dislike

app = Flask('')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    ytlink = request.form['vid']
    return render_template('result.html', stats=return_dislike(ytlink))


def run():
    app.run(host='0.0.0.0')


def show_site():
    t = Thread(target=run)
    t.start()


show_site()
