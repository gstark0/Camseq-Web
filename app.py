from flask import Flask, render_template, request, session, redirect
import db_manager as dbmngr
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/public')
def public():
    return render_template('public.html')

@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/cameras')
def cameras():
	user_logged = session.get('logged_in')
	if user_logged:
		cameras = dbmngr.get_cameras_by_user_id(user_logged)
		return render_template('cameras.html', cameras=cameras)
	else:
		return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		# If user is already logged in, just redirect to "cameras" page
		user_logged = session.get('logged_in')
		if user_logged:
			return redirect('/cameras')
		else:
			return render_template('login.html')

	elif request.method == 'POST':
		# Get form data from login page
		login = request.values.get('login')
		password = request.values.get('password')

		# Check if user exists
		user = dbmngr.get_user(login, password)
		if user:
			session['logged_in'] = user['user_id']
			return redirect('/cameras')
		else:
			return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0')