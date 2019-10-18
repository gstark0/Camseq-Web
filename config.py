import os

SECRET_KEY = os.urandom(24)
db_name = 'database.db'

width = 128
height = 128

training_paths = [
	['../fights/fight', '../dataset/fight'],
	['../fights/noFight', '../dataset/noFight']
]