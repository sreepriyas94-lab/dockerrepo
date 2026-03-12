from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Docker"

@app.route("/about")
def about():
    return "about Docker"

@app.route("/career")
def career():
    return "career"

app.run (host = "0.0.0.0", port = 5000)
