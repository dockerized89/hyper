import os
import sys
sys.path.append(os.getcwd())

from flask import Flask, render_template
from classes import Bucket
from classes import Author

# app variable containing a Flask object
app = Flask(__name__)

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

# Main method that is that one that is actually executed
if __name__ == "__main__":
    # Tell the app to start
    app.run(debug=True)