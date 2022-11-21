from flask import Flask
app2 = Flask(__name__)
@app2.route("/")
def home():
    return "Hello, Flask is running on app!"