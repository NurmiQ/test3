from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


app.run()
