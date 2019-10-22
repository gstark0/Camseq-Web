from flask import Flask, render_template, request, session, redirect
import db_manager as dbmngr
from config import SECRET_KEY, footage_path
from utils import img_to_array, resize_img
import urllib.request
from model import Model
import numpy as np
import cv2
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# AI Models
fights_detector = Model()
fights_detector.load_model('./models/fights_detector.h5')

fire_detector = Model()
fights_detector.load_model('./models/fire_detector.h5')

def save_footage(incident_id, original_img):
	incident_path = '%s/%s' % (footage_path, incident_id)
	os.mkdir(incident_path)
	cv2.imwrite('%s/img.jpg' % incident_path, original_img)


def process_cameras():
	cameras = dbmngr.get_all_cameras()

	# Download a frame from each of the cameras added
	for camera in cameras:
		camera_id = camera['camera_id']
		camera_url = camera['url']

		original_img, img = resize_img(in_url=camera_url)
		img_to_predict = np.asarray([img])
		
		fight_prediction = fights_detector.predict(img_to_predict)
		print('Fight prediction: ', fight_prediction, np.argmax(fight_prediction))
		fire_prediction = fire_detector.predict(img_to_predict)
		print('Fire prediction: ', fire_prediction, np.argmax(fire_prediction))

		fight_prediction = np.argmax(fight_prediction)
		fire_prediction = np.argmax(fire_prediction)

		if fight_prediction == 0:
			print('Camera #%s - Fight detected!' % camera_id)
			incident_id = dbmngr.add_incident(camera_id, 'warning', 'Wykryto bójkę')
			save_footage(incident_id, original_img)
		if fire_prediction == 0:
			print('Camera #%s - Fire detected!' % camera_id)
			incident_id = dbmngr.add_incident(camera_id, 'danger', 'Wykryto płomień')
			save_footage(incident_id, original_img)


process_cameras()

# --------- WEB ---------
@app.route('/public')
def public():
    return render_template('public.html')

@app.route('/preview/<int:camera_id>')
def preview(camera_id):
	user_logged = session.get('logged_in')
	if user_logged:
		camera_info = dbmngr.get_camera_by_id(camera_id)
		camera_incidents = dbmngr.get_incidents_by_camera(camera_id)
		return render_template('preview.html', camera_info=camera_info, camera_incidents=camera_incidents)
	else:
		return redirect('/login')

@app.route('/cameras')
def cameras():
	user_logged = session.get('logged_in')
	if user_logged:
		cameras = dbmngr.get_cameras_by_user_id(user_logged)
		return render_template('cameras.html', cameras=cameras)
	else:
		return redirect('/login')

@app.route('/logout')
def logout():
	session['logged_in'] = False
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