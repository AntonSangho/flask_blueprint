# from flask import Flask
from main import app

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9999, debug = True)
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask"