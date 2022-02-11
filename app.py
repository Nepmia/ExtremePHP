from urllib import response
from flask import Flask, render_template, abort, Response, request

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("home.html")
