from flask import Flask, render_template

app = Flask(__name__)

@app.route('/public')
def public():
    return render_template('public.html')

@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/cameras')
def cameras():
    return render_template('cameras.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')