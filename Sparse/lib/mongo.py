from pymongo import MongoClient
import pprint
import datetime

# please note, dont connect to the driver if this function inside your loop
def mongo_conn():
	conn_read = MongoClient('mongodb://10.10.21.4:27017,10.10.21.212:27017/?connectTimeoutMS=300000')
	return conn_read.db_Training_Python

# function mongo_local_date() convert mongo date to local date 
# var date 	: mongo date format see user_explorer_activities:232
# var utf 	: default gmt+7
def mongo_local_date(date, _format = False, gmt = 7):
	if(date == False or date == "unknown" or date == None):
		return "Unknown"
	else:
		date = date + datetime.timedelta(hours=gmt)

		if(_format != False):
			return date.strftime(_format)
		else:
			return date

