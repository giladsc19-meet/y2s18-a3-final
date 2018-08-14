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
			print(user)
			session['user_id'] = user.id
			print(session['user_id'])
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
		content = request.form.get('content', False)
		image_url = request.form.get('image_url', False)
		print(image_url)
		print(content)
		print(session.get('user_id'))
		post = make_post(session.get('user_id'), content, image_url)
		feed = get_posts()
		return render_template('home.html', feed = feed )
 
 #this is for the profile page

@app.route('/user/<string:user_name>')
def display_user(user_name):
    return render_template('profile.html', user=get_by_user_name(user_name))





if __name__ == "__main__":
    app.run(debug=True)
