import cv2
import os

paths = [
	['./fights/fight', './dataset/fight'],
	['./fights/noFight', './dataset/noFight']
]

# Save the image every x frames
x_frames = 10

for path in paths:
	filenames = os.listdir(path[0])

	index = 0
	for filename in filenames:
		vid = cv2.VideoCapture('%s/%s' % (path[0], filename))

		while(True):
			# Extract images
			ret, frame = vid.read()
			# End of frames
			if not ret:
				break

			if index % x_frames != 0:
				index += 1
				continue

			# Save images
			name = '%s/img%s.jpg' % (path[1], index)
			print('Saving... %s' % name)
			frame = cv2.resize(frame, (128, 128))
			cv2.imwrite(name, frame)

			# Next frame
			index += 1