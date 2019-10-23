import sqlite3
from datetime import datetime
from config import db_name, incident_descriptions
from utils import fetch_location
import requests

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

def add_incident(camera_id, type_, description, camera_coord):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		curr_time = datetime.now()
		curr_time = curr_time.strftime('%d/%m/%Y - %H:%M:%S')
		cur.execute('INSERT into incidents (camera_id, type, description, time) VALUES (?, ?, ?, ?)', (camera_id, type_, description, curr_time))
		incident_id = cur.lastrowid
		conn.commit()

		lat, lon = camera_coord.split(', ')
		city, district = fetch_location(lat, lon)
		cur.execute('SELECT * FROM public_data WHERE city=? AND district=?', (city, district))
		result = cur.fetchone()
		print(result)
		conn.commit()

		if not result:
			if description == incident_descriptions['fight']:
				cur.execute('INSERT into public_data (city, district, fights, car_crashes, fires, weapons) VALUES (?, ?, 1, 0, 0, 0)', (city, district))
			elif description == incident_descriptions['car_crash']:
				cur.execute('INSERT into public_data (city, district, fights, car_crashes, fires, weapons) VALUES (?, ?, 0, 1, 0, 0)', (city, district))
			elif description == incident_descriptions['fire']:
				cur.execute('INSERT into public_data (city, district, fights, car_crashes, fires, weapons) VALUES (?, ?, 0, 0, 1, 0)', (city, district))
			elif description == incident_descriptions['weapon']:
				cur.execute('INSERT into public_data (city, district, fights, car_crashes, fires, weapons) VALUES (?, ?, 0, 0, 0, 1)', (city, district))
		else:
			if description == incident_descriptions['fight']:
				cur.execute('UPDATE public_data SET fights=fights+1')
			elif description == incident_descriptions['car_crash']:
				cur.execute('UPDATE public_data SET car_crashes=car_crashes+1')
			elif description == incident_descriptions['fire']:
				cur.execute('UPDATE public_data SET fires=fires+1')
			elif description == incident_descriptions['weapon']:
				cur.execute('UPDATE public_data SET weapons=weapons+1')

	return incident_id

def count_incidents(camera_id):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM incidents WHERE type="warning" AND camera_id=?', (camera_id,))
		warnings = len(cur.fetchall())

		cur.execute('SELECT * FROM incidents WHERE type="danger" AND camera_id=?', (camera_id,))
		dangers = len(cur.fetchall())

		conn.commit()
		cur.execute('UPDATE cameras SET dangers=?, warnings=? WHERE camera_id=?', (dangers, warnings, camera_id))
	return 1

def get_data_by_region(city, district):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT * FROM public_data WHERE city=? AND district=?', (city, district))
		data = cur.fetchone()
	
	if data:
		return data['fires'], data['weapons'], data['fights'], data['car_crashes']
	else:
		return 'Brak danych', 'Brak danych', 'Brak danych', 'Brak danych'

def get_coord_list():
	with sqlite3.connect(db_name) as conn:
		cur = conn.cursor()

		cur.execute('SELECT camera_id FROM incidents')
		camera_ids = cur.fetchall()
		conn.commit()

		cur.execute('SELECT camera_id FROM cameras')
		camera_ids += cur.fetchall()
		
		camera_ids = [camera_id[0] for camera_id in camera_ids]
		print(camera_ids)
		conn.commit()

		last_id = -1
		coord_list = []
		for camera_id in camera_ids:
			if last_id == camera_id:
				coord_list[-1][2] += 0.2
			else:
				cur.execute('SELECT coordinates FROM cameras WHERE camera_id=?', (camera_id,))
				result = cur.fetchone()[0]
				coord_list.append([float(result.split(', ')[0]), float(result.split(', ')[1]), 0.2])
				last_id = camera_id
				conn.commit()
	print(coord_list)
	return coord_list