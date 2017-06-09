'''Main server page for Coding Dojo Flask Fundamentals "Landing Page" assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def landingpage():
    return render_template("index.html")

@app.route('/ninjas')

def ninjapage():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def dojosform():
    return render_template("dojos.html")

app.run(debug=True)

