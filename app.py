from databases import *
from flask import Flask, render_template, url_for,request,redirect
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', users=query_all())
@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		
		name= request.form['username']
		year= request.form['password']
		add_users(user_name,password)

		return render_template('add.html')

	
@app.route('/user/<int:user_name>')
def display_user(user_name):
    return render_template('login.html', user=query_by_user_name(user_name))
@app.route('/delete/<int:user_name>', methods=['POST'])
def delete(user_namr):
    delete_user(user_name)
    return redirect(url_for('login.html'))
		

app.run(debug=True)