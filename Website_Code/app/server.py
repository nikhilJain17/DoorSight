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

@app.route('/pickmode', methods=['POST'])
def pickmode():
	if request.form['mode'] == 'lockunlock':
		print 'mode 1'
	elif request.form['mode'] == 'inputfaces':
		print 'mode 2'

	return 'ok'

# FOR DEV ONLY
@app.route('/shutdown', methods=['GET'])
def shutdown():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running')
	func() 

# have some function to read the mode form's data
# store the mode in a variable
# depending on which mode is selected, emit an event to the rpi

# pass the events and event handlers to the websocket
@socketio.on('ping', namespace='/')
def connected():
	print 'Somebody Connected!'
