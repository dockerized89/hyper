from flask import Flask, render_template
# app variable containing a Flask object
app = Flask(__name__)

# The route in URL to listen on.
@app.route("/")
@app.route("/index")
def index():
    # Return a rendering of template found in templates/index.html
    return render_template("index.html")

# Main method that is that one that is actually executed
if __name__ == "__main__":
    # Tell the app to start
    app.run(debug=True)