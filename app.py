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
			return render_template('home.html',feed = get_posts())
		
		else:
			x = "wrong password or user_name"
			return render_template('login.html', message=x)

@app.route('/signup', methods=['GET', 'POST'])
def add_users():
	if request.method == 'GET':
		return render_template('sign_up.html')
	else:
		first_name= request.form['first_name']
		last_name= request.form['last_name']
		birthdate= request.form['birthdate']
		user_name= request.form['user_name']
		password= request.form['password']
		status = add_user(first_name,last_name,birthdate,user_name,password)
		feed = get_posts()
		if status:
			return render_template('home.html', feed = feed)
		else:
			return render_template('sign_up.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	user_name = ""
	

	if request.method == 'GET':
		user_name = request.form['user_name']
		password = request.form['password']
		if(check_user(user_name, password)):
			feed = get_posts()
			print("home is where you are")
			return render_template('home.html', feed=feed)
		else:
			return redirect(url_for('login'))
	else:
		content = request.form.get('text', False)
		image_url = request.form.get('image_url', False)
		print(image_url)
		print(content)
		# print(session.get('user_id'))
		post = make_post(user_name, content, image_url)
		feed = get_posts()
		return render_template('home.html', feed = feed )

# @app.route('/home/<string:user_name>/<string:password>', methods=['GET', 'POST'])
# def home():
# 	if request.method == 'GET':
# 		feed = get_posts()
# 		print("home is where you are")
# 		return render_template('home.html', feed=feed)
# 	else:
# 		content = request.form.get('text', False)
# 		image_url = request.form.get('image_url', False)
# 		print(image_url)
# 		print(content)
# 		print(session.get('user_id'))
# 		post = make_post(session.get('user_id'), content, image_url)
# 		feed = get_posts()
		# return render_template('home.html', feed = feed )

 #this is for the profile page

@app.route('/<string:user_name>')
def display_user(user_name):

	user= get_by_user_name(user_name)
	return render_template('profile.html', user=user)


@app.route('/about')
def about():
	return render_template('whower.html')


if __name__ == "__main__":
	app.run(debug=True)
