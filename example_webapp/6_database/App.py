import os
import sys
sys.path.append(os.getcwd())
os.environ['PYTHONPATH'] += os.getcwd()

from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from classes import Bucket
from classes import Author

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


# The route in URL to listen on.
@app.route("/")
@app.route("/index")
def index():
    buckets = create_dummy_users()

    return render_template("index.html",
                           title="My fancy title",
                           page="home", buckets=buckets)


#ShowSignup method
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

#Signup method
@app.route('/signUp',methods=['POST'])
def signUp():
    # read the posted values from form
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

# Main method that is that one that is actually executed
if __name__ == "__main__":
    # Tell the app to start
    app.run(debug=True)