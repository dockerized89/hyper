from flask import Flask
# app variable containing a Flask object
app = Flask(__name__)

# The route in URL to listen on.
@app.route("/")
@app.route("/index")
def main():
    return "Hello World!"

# Tell the app to start
app.run(debug=True)
