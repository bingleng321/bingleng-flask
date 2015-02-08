#!/usr/bin/python

from flask import Flask,render_template,request,redirect

app_ming = Flask(__name__)
app_ming.vars = {}

app_ming.questions = {}
app_ming.questions['How many eyes do you have?'] = ('1','2','3')
app_ming.questions['Which fruit do you like best?'] = ('banana','apple','orange')
app_ming.questions['Do you like cupcakes'] = ('Yes','No','Maybe')

app_ming.nquestions = len(app_ming.questions)

@app_ming.route('/index_ming',methods = ['GET','POST'])
def index_ming():
	nquestions = app_ming.nquestions
	if request.method == 'GET':
		return render_template('userinfo_ming.html',num = nquestions)
	else:
		app_ming.vars['name'] = request.form['name_ming']
		app_ming.vars['age'] = request.form['age_ming']

		f = open('%s_%s.txt'%(app_ming.vars['name'],app_ming.vars['age']),'w')
		f.write('Name:%s\n'%(app_ming.vars['name']))
		f.write('Age:%s\n\n'%(app_ming.vars['age']))
		f.close()
		return redirect('/main_ming')


@app_ming.route('/main_ming')
def main_ming2():
	if len(app_ming.questions) == 0:
		return render_template('end_ming.html')
	else:
		return redirect('/next_ming')


@app_ming.route('/next_ming',methods=['GET','POST'])
def next_ming():
	if request.method == 'GET':
		n = app_ming.nquestions - len(app_ming.questions) + 1
		q = app_ming.questions.keys()[0]
		a1,a2,a3 = app_ming.questions.values()[0]

		app_ming.currentq = q
		return render_template('layout_ming.html',num = n,question = q,\
				ans1 = a1, ans2 = a2, ans3 = a3)
	else:
		f = open('%s_%s.txt'%(app_ming.vars['name'],app_ming.vars['age']),'a')
		f.write('%s\n'%(app_ming.currentq))
		f.write('%s\n\n'%(request.form['answer_form_layout_ming']))
		f.close()

		del app_ming.questions[app_ming.currentq]
		return redirect('/main_ming')

if __name__ == "__main__":
	app_ming.run(debug=True)
