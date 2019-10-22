import cv2
import os
from config import training_paths

# Save the image every x frames
x_frames = 3

# Resize images
w = 128
h = 128

def preprocess_data(paths):
	for path in paths:
		filenames = os.listdir(path[0])

		index = 0
		for filename in filenames:
			in_path = '%s/%s' % (path[0], filename)
			if '.mp4' in filename:
				vid = cv2.VideoCapture(in_path)

				while(True):
					# Extract images
					ret, frame = vid.read()
					# End of frames≠
					if not ret:
						break

					if index % x_frames != 0:
						index += 1
						continue

					# Save images
					name = '%s/img%s.jpg' % (path[1], index)
					print('Saving... %s' % name)
					frame = cv2.resize(frame, (w, h))
					cv2.imwrite(name, frame)

					# Next frame
					index += 1
			else:
				img = cv2.imread(in_path)
				resized_img = cv2.resize(img, (w, h))
				name = '%s/img%s.jpg' % (path[1], index)
				cv2.imwrite(name, resized_img)
				index += 1

preprocess_data(training_paths)