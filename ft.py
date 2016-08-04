from flask import Flask, render_template, request, redirect, url_for, escape
from pyo import *
import os

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("x.html")


############
# IFGUARD #
############
if __name__ == '__main__':
    app.run(debug=True)


