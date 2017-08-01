from Sparse.lib.mongo import *

db = mongo_conn()

def get_total_session():
	count_session = db.piwik_log_visit.find().count()

	return count_session
