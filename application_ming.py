#!/usr/bin/python

from flask import Flask,render_template,request

app_ming = Flask(__name__)

@app_ming.route('/index_ming',methods = ['GET','POST'])
def index_ming():
	nquestions = 5
	if request.method == 'GET':
		return render_template('userinfo_ming.html',num = nquestions)
	else:
		return 'request.method was not a GET!'

if __name__ == "__main__":
	app_ming.run(debug=True)
