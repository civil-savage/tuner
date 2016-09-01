import csv
import os
import time
from flask import Flask, render_template, request, redirect, url_for, escape
from pyo import *


app = Flask(__name__)
app.debug = True


# def ser():
#     s = Server(audio="offline_nb").boot()
#     path = os.path.join(os.path.expanduser("~/xdev/static"), "synth.ogg")
#     s.recordOptions(dur=5, filename=path, fileformat=7, sampletype=1)
#     s.start()
#     # Creates an amplitude envelope
#     amp = Fader(fadein=1, fadeout=1, dur=10, mul=0.3).play()

#     # A Simple synth
#     lfo = Sine(freq=[0.15, 0.16]).range(1.25, 1.5)
#     fm2 = CrossFM(carrier=200, ratio=lfo, ind1=10, ind2=2, mul=amp).out()
#     time.sleep(5)



    
# ser()
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


