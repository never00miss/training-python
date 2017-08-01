from Sparse import app
from flask.json import jsonify

@app.route('/')
@app.route('/home')
def home():
	return jsonify({'status' : 1, 'message' : 'you are on home page'})