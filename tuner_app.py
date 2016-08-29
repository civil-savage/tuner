import csv
import os
from flask import Flask, render_template, request, redirect, url_for, escape
from pyo import *


app = Flask(__name__)
app.debug = True

with open('notes.csv', 'rb') as notefile:
    csv = csv.reader(notefile)
    notes = []
    for row in csv:
        notes.append(row)


@app.route('/', methods=['GET', 'POST'])
def main():
    
    return render_template("x.html", notes=notes)

############
# IFGUARD #
############
if __name__ == '__main__':
    app.run(debug=True)


