from tensorflow import keras
import os
import cv2
import numpy as np
from config import width, height
import urllib.request
import requests
import imutils

img_preprocessing = keras.preprocessing.image

def fetch_location(lat, lon):
	r = requests.get('https://locationiq.com/v1/reverse_sandbox.php?format=json&lat=%s&lon=%s&accept-language=en' % (lat, lon))
	r = r.json()['address']
	city = r['city']
	district = r['city_district']

	return city, district

# Resize an image to correct size
def resize_img(in_path='', in_url=''):
	if in_path != '':
		img = cv2.imread(in_path)
	elif in_url != '':
		req = urllib.request.urlopen(in_url)
		arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
		img = cv2.imdecode(arr, -1)

	resized_img = cv2.resize(img, (width, height))
	resized_img = resized_img[...,::-1].astype(np.float32) / 255.0

	return img, resized_img

# Load cascade and detect gun on the image provided
def detect_gun(img):
	gun_cascade = cv2.CascadeClassifier('cascade.xml')
	#img = imutils.resize(img, width=500)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize = (50, 50))

	gun_exist = False
	if len(gun) > 0:
		gun_exist = True

	return gun_exist

# Load and convert image to NumPy array
def img_to_array(path):
	img = img_preprocessing.load_img(path)
	img_array = img_preprocessing.img_to_array(img) / 255.0
	return img_array


# Load data
def get_data(paths):

	x = []
	y = []

	label = 0
	for path in paths:
		filenames = os.listdir(path[1])

		for filename in filenames:
			img_array = img_to_array('%s/%s' % (path[1], filename))
			x.append(img_array)
			y.append(label)

		label += 1
	return np.asarray(x), np.asarray(y)



