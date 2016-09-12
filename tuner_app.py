import csv
import os
import time
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
    return render_template("tuner.html", notes=notes)


# IFGUARD #
if __name__ == '__main__':
    app.run(debug=True)

# Need this for translating names later
# def rename(name):
#     name = name.replace('#','s')
#     name = name.replace('b','f')
#     name = name.replace('/','_')
#     return name
