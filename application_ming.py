#!/usr/bin/python

from flask import Flask,render_template,request,redirect

app_ming = Flask(__name__)
app_ming.vars = {}

@app_ming.route('/next_ming',methods=['POST'])
def next_ming():
	return redirect('/usefulfunction_ming')

@app_ming.route('/usefulfunction_ming',methods=['GET','POST'])
def usefulfunction_ming():	
	return render_template('layout_ming.html',num=1,question='which fruit do you like \
			best?',ans1='apple',ans2='banana',ans3='orange')

@app_ming.route('/index_ming',methods = ['GET','POST'])
def index_ming():
	nquestions = 5
	if request.method == 'GET':
		return render_template('userinfo_ming.html',num = nquestions)
	else:
		app_ming.vars['name'] = request.form['name_ming']
		app_ming.vars['age'] = request.form['age_ming']

		f = open('%s_%s.txt'%(app_ming.vars['name'],app_ming.vars['age']),'w')
		f.write('Name:%s\n'%(app_ming.vars['name']))
		f.write('Age:%s\n\n'%(app_ming.vars['age']))
		f.close()

		return render_template('layout_ming.html',num=1,question='How many eyes do you have?',ans1='1',ans2='2',ans3='3')

if __name__ == "__main__":
	app_ming.run(debug=True)
