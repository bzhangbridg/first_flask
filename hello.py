import os
from flask import Flask, render_template, send_from_directory
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap 
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
	return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name = name)

@app.errorhandler(404) 
def page_not_found(e):
	return render_template('404.html'), 404
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	manager.run()
