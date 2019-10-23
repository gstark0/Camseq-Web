import os

SECRET_KEY = os.urandom(24)
db_name = 'database.db'

footage_path = './footage'

width = 128
height = 128

incident_descriptions = {
	'fire': 'Wykryto pożar',
	'weapon': 'Wykryto broń',
	'fight': 'Wykryto bójkę',
	'car_crash': 'Wykryto zdarzenie drogowe'
}

'''
training_paths = [
	['../fights/fight', '../dataset/fight'],
	['../fights/noFight', '../dataset/noFight']
]


training_paths = [
	['../fire/fire', '../dataset/fire'],
	['../fire/noFire', '../dataset/noFire']
]
'''

training_paths = [
	['../crashes/crash', '../dataset/crash'],
	['../crashes/noCrash', '../dataset/noCrash']
]