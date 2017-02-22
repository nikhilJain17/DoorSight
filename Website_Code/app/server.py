# flask app
# whats up doc

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
	print 'Hello!'
	return render_template('login.html')