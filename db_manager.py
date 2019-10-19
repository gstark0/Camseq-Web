import sqlite3
from config import db_name

# Getting column names
def dict_factory(cursor, row):
	d = {}
	for idx,col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

# Get user_id with provided login and password
def get_user(login, password):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT user_id FROM users WHERE login=? AND password=?', (login, password))
		result = cur.fetchone()
	return result

def get_cameras_by_user_id(user_id):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM cameras WHERE user_id=?', (user_id,))
		results = cur.fetchall()
	return results

def get_camera_by_id(camera_id):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM cameras WHERE camera_id=?', (camera_id,))
		result = cur.fetchone()
	return result	

def get_incidents_by_camera(camera_id):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM incidents WHERE camera_id=?', (camera_id,))
		results = cur.fetchall()
	return results