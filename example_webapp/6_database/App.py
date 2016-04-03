import os
import sys

sys.path.append(os.getcwd())
os.environ['PYTHONPATH'] += os.getcwd()

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from classes import Bucket
from classes import Author
# Database stuff
from database import init_db
from models import User
from database import db_session

# app variable containing a Flask object
app = Flask(__name__)
# We will import our config file here.
app.config.from_object('config')
# Create the database object
db = SQLAlchemy(app)


def create_dummy_users():
    buckets = []
    # Buckets wants Authors, lets create them first
    author_1 = Author("Anna")
    author_2 = Author("Kalle")

    # Now lets create the buckets
    bucket_1 = Bucket(author_1, "Bucket created by {0}".format(author_1.get_name()))
    bucket_2 = Bucket(author_2, "Bucket created by {0}".format(author_2.get_name()))

    buckets.append(bucket_1)
    buckets.append(bucket_2)

    return buckets


# The route in URL to listen on.
@app.route("/")
@app.route("/index")
def index():
    buckets = create_dummy_users()

    return render_template("index.html",
                           title="My fancy title",
                           page="home", buckets=buckets)


# ShowSignup method
@app.route('/showSignUp', methods=['GET', 'POST'])
def showSignUp():
    if request.method == 'POST':
        # read the posted values from form
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        print(_name)
        print(_email)
        print(_password)

        # validate the received values
        if _name and _email and _password:
            user = User(_name, _email, _password)
            db_session.add(user)
            db_session.commit()

            return render_template('signup.html',
                                   page='signup',
                                   title='my fancy signup page',
                                   success=True)
        else:
            return render_template('signup.html',
                                   page='signup',
                                   title='my fancy signup page',
                                   success=False)
    else:

        return render_template('signup.html',
                               page='signup',
                               title='my fancy signup page')


def get_users():
    user_list = User.query.all()
    for user in user_list:
        User.query
    return User.query.all()


@app.route('/list_users')
def list_users():
    return render_template('list_users.html',
                           users=get_users(),
                           page='User list',
                           title='My fancy user list')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    # Tell the app to start
    init_db()
    app.run(debug=True)
