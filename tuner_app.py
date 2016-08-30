import csv
import os
from flask import Flask, render_template, request, redirect, url_for, escape
from pyo import *


app = Flask(__name__)
app.debug = True


def ser():
    s = Server().boot()
    path = os.path.join(os.path.expanduser("~/tuner/tuner/static"), "synth.wav")
    s.recordOptions(dur=10, filename=path, fileformat=0, sampletype=1)
    a = Sine(500,.2)
    s.recstart()


with open('notes.csv', 'rb') as notefile:
    csv = csv.reader(notefile)
    notes = []
    for row in csv:
        notes.append(row)


@app.route('/', methods=['GET', 'POST'])
def main():
    ser()
    return render_template("x.html", notes=notes)


# IFGUARD #
if __name__ == '__main__':
    app.run(debug=True)


