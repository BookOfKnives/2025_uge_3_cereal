#2909 2025
#11:20

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

@app.route("/api")
def data():
    return "<p>no more data</p>"

#Crud calls

#database cnnection: