# flask app
# whats up doc

from flask import Flask, render_template, request
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def welcome():
	print 'Hello!'
	# serve up the login page
	return render_template('login.html')


@app.route('/attempt_login', methods=['POST'])
def attempt_login():
	print 'test'
	print request.args
	return render_template('selectMode.html')