from Sparse import app
from flask.json import jsonify

from Sparse.model import piwik_log_visit

@app.route('/')
@app.route('/home')
def home():
	return jsonify({'status' : 1, 'message' : 'you are on home page'})

@app.route('/get_total_session')
def get_total_session():
	total_session = piwik_log_visit.get_total_session()

	return jsonify({'status' : 1, 'total_session' : total_session})