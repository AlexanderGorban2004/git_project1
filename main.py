import requests
from flask import Flask
from flask import request, url_for, render_template
import json
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import random

app = Flask(__name__)


@app.route('/')
@app.route('/member')
def member():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    name = "dfg"
    prof = "fgg"
    for user in session.query(User).filter(User.id == random.randint(1, 10)):
        name = user.name
        surname = user.surname
        prof = user.speciality.split()
        prof.sort()
        prof = " ".join(prof)
    return render_template('login.html', pict=url_for('static', filename='img/mg1.jpg'), name=(name + " " + surname), prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
