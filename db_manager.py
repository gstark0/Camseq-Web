import sqlite3
from datetime import datetime
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

def get_all_cameras():
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM cameras')
		results = cur.fetchall()
	return results

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

def add_incident(camera_id, type_, description):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		curr_time = datetime.now()
		curr_time = curr_time.strftime('%d/%m/%Y - %H:%M:%S')
		cur.execute('INSERT into incidents (camera_id, type, description, time) VALUES (?, ?, ?, ?)', (camera_id, type_, description, curr_time))
		incident_id = cur.lastrowid
	return incident_id

def count_incidents(camera_id):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM incidents WHERE type="warning"')
		warnings = len(cur.fetchall())

		cur.execute('SELECT * FROM incidents WHERE type="danger"')
		dangers = len(cur.fetchall())

		conn.commit()
		cur.execute('UPDATE cameras SET dangers=?, warnings=? WHERE camera_id=?', (dangers, warnings, camera_id))
	return 1