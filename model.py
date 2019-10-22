from tensorflow import keras
import tensorflow as tf
from config import *
import utils

class Model:

	def __init__(self):
		self.model = keras.Sequential([
			keras.layers.Convolution2D(32, 3, 3, input_shape=(width, height, 3), activation=tf.nn.relu),
			keras.layers.MaxPooling2D(pool_size=(2, 2)),

			keras.layers.Flatten(),
			keras.layers.Dense(512, activation=tf.nn.relu),
			keras.layers.Dense(2, activation=tf.nn.softmax)
		])

	def load_model(self, path):
		print('Loading Model from "%s"...' % path)
		self.model.load_weights(path)
		print('Model loaded!')

	def save_model(self, path):
		print('Saving model to "%s"...' % path)
		self.model.save_weights(path)
		print('Model saved!')

	def train(self, x_train, y_train, epochs=5, lr=0.001):
		self.model.compile(optimizer=keras.optimizers.Adam(lr=lr), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		self.model.fit(x_train, y_train, epochs=epochs)

		print('Model training finished!')

	def predict(self, x):
		return self.model.predict(x)


#m = Model()
#x_train, y_train = utils.get_data(training_paths)
#m.load_model('fights_detector.h5')
#print(m.predict(x_train))
#m.train(x_train, y_train, epochs=4)
#m.save_model('fire_detector.h5')