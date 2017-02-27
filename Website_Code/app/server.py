# flask app
# dependencies: flask, flask-socketio
from flask import Flask, render_template, request
from flask_socketio import SocketIO

# init the libraries
app = Flask(__name__)
app.url_map.strict_slashes = False

socketio = SocketIO(app)
 
# pass the routes and route handlers to the flask app
@app.route('/')
def welcome():
	print 'Hello!'
	# serve up the login page
	return render_template('login.html')


@app.route('/attempt_login', methods=['POST'])
def attempt_login():
	print 'test'
	# hash or something later?
	username = str(request.form.getlist('username')[0])
	password = str(request.form.getlist('password')[0])

	# for testing only, delete later
	print "U: " + username + '\nP: ' + password 
	return render_template('selectMode.html')

# pass the events and event handlers to the websocket
@socketio.on('connect', namespace='/')
def connected():
	print 'somebody connected!'

	# make sure the raspi connects with sockets to this server