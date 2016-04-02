from flask import Flask
# app variable containing a Flask object
app = Flask(__name__)

# The route in URL to listen on.
@app.route("/")
@app.route("/index")
def main():
    return "Hello World!"


# Main method that is that one that is actually executed
if __name__ == "__main__":
    # Tell the app to start
    app.run(debug=True)