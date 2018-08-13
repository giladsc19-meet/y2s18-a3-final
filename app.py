from databases import *
from flask import Flask, render_template, url_for,request,redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		
		user_name= request.form['user_name']
		password= request.form['password']
		status = add_user(user_name,password)
		
		if status:
			return render_template('home.html')
		else:
			return render_template('login.html')




# this is for the home page (feed page)

@app.route('/home/<string:user_name>/<string:password>')
def home(user_name, password):
    return render_template('home.html', user_name = user_name, password = password)

# this is for the profile page

@app.route('/user/<string:user_name>')
def display_user(user_name):
    return render_template('login.html', user=get_by_user_name(user_name))

# this is for the 

@app.route('/delete/<string:user_name>')
def delete(user_name):
    delete_user(user_name)
    return redirect(url_for('login.html'))
		
if __name__ == "__main__":
    app.run(debug=True)
