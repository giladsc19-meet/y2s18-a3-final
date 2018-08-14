from databases import *
from flask import session, Flask, render_template, url_for,request,redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user_name = request.form['user_name']
		password= request.form['password']
		if check_user(user_name, password)==True:
			user = get_by_user_name(user_name)
			session['user_id'] = user.id
			return redirect(url_for('home'))
		else:
			x = "wrong password or user_name"
			return render_template('login.html', message=x)

@app.route('/signup', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('sign_up.html')
	else:
		
		user_name= request.form['user_name']
		password= request.form['password']
		status = add_user(user_name,password)
		
		if status:
			return redirect(url_for('login'))
		else:
			return render_template('sign_up.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		print("home 1")
		feed = get_posts()
		print("home is where you are")
		return render_template('home.html', feed=feed)
	else:
		text = request.form['text']
		image_url = request.form['image_url']
		post = make_post(session['user_id'], text, image_url)
		return render_template('home.html', post = post )
 
 #this is for the profile page

@app.route('/user/<string:user_name>')
def display_user(user_name):
    return render_template('home.html', user=get_by_user_name(user_name))




@app.route('/yyy')
def dis():
	return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
