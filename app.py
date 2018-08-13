from databases import *
from flask import Flask, render_template, url_for,request,redirect
app = Flask(__name__)

########################################################################################## Dont care about the above !


@app.route('/', methods=['GET', 'POST'])
def login():

	if request.method == 'GET':
		return render_template('login.html')

	if request.method == 'POST':
		user_name= request.form['user_name']
		password= request.form['password']
		status = add_user(user_name,password)
		
		if status:
			return render_template('home.html', user = new_user)
		else:
			return render_template('login.html')


# this is for the profile page

@app.route('/user/<string:user_name>')
def display_user(user_name):
    return render_template('login.html', user=get_by_user_name(user_name))


if __name__ == "__main__":
    app.run(debug=True)
