from flask import Flask, render_template
# app variable containing a Flask object
app = Flask(__name__)

# The route in URL to listen on.
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           title="My fancy title",
                           page="home")

# Main method that is that one that is actually executed
if __name__ == "__main__":
    # Tell the app to start
    app.run(debug=True)