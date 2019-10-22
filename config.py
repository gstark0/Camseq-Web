import os

SECRET_KEY = os.urandom(24)
db_name = 'database.db'

footage_path = './footage'

width = 128
height = 128

'''
training_paths = [
	['../fights/fight', '../dataset/fight'],
	['../fights/noFight', '../dataset/noFight']
]
'''

training_paths = [
	['../fire/fire', '../dataset/fire'],
	['../fire/noFire', '../dataset/noFire']
]