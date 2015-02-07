#!/usr/bin/python

from flask import Flask,render_template

app_ming = Flask(__name__)

@app_ming.route('/index_ming')
def index_ming():
	nquestions = 5
	return render_template('userinfo_ming.html',num = nquestions)

if __name__ == "__main__":
	app_ming.run(debug=True)
