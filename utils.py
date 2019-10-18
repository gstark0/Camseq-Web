from tensorflow import keras
import os
import numpy as np

img_preprocessing = keras.preprocessing.image

# Load and convert image to NumPy array
def img_to_array(path):
	img = img_preprocessing.load_img(path)
	img_array = img_preprocessing.img_to_array(img)
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



