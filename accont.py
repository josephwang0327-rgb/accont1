from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
from pandas import pandas
import numpy as np

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/accont",methods=['post'])
def accont():
    return render_template("accont.html")

@app.route("/show",methods=['post'])
def show():
    now = datetime.now()
    amount = request.values['amount']
    return render_template("show.html",**locals())

if __name__ == '__main__' :
    app.run()