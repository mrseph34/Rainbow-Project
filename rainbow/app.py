from flask import Flask, render_template, json, jsonify, request, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
 return render_template('home.html', txt="Welcome to Joseph's Rainbow Project")

@app.route('/rainbow')
def rainbow():
 return render_template('rainbow.html', txt="Welcome to Joseph's Rainbow Project", colors=["red","orange","yellow","green","blue","indigo","violet"])

@app.route('/red')
def red():
 return render_template('rainbow_template.html', color="red")

@app.route('/orange')
def orange():
 return render_template('rainbow_template.html', color="orange")

@app.route('/yellow')
def yellow():
 return render_template('rainbow_template.html', color="yellow")

@app.route('/green')
def green():
 return render_template('rainbow_template.html', color="green")

@app.route('/blue')
def blue():
 return render_template('rainbow_template.html', color="blue")

@app.route('/indigo')
def indigo():
 return render_template('rainbow_template.html', color="indigo")

@app.route('/violet')
def violet():
 return render_template('rainbow_template.html', color="violet")

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0') 