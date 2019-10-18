import sqlite3
from config import db_name

# Getting column names
def dict_factory(cursor, row):
	d = {}
	for idx,col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def get_user(login, password):
	with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		conn.row_factory = dict_factory
		cur = conn.cursor()

		cur.execute('SELECT user_id FROM users WHERE login=? AND password=?', (login, password))
		result = cur.fetchone()
	return result