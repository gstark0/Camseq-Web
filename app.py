from flask import Flask, render_template
from config import db_name

app = Flask(__name__)

@app.route('/public')
def public():
    return render_template('public.html')

@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/cameras')
def cameras():
	#with sqlite3.connect(db_name) as conn:
		# SQLite3 doesn't return keys by default
		#conn.row_factory = dict_factory
		#cur = conn.cursor()
    return render_template('cameras.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')