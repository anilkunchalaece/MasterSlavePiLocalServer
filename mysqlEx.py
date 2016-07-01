#! /usr/bin/python
import MySQLdb

db = MySQLdb.connect("localhost","anil","raspberry","sensorData")

curs = db.cursor()

try:

	curs.execute("""INSERT INTO sensorData.sensorDataTable 
		values('E','2016-06-29 17:08:18.995884',1,6)""")
	db.commit()
	print "Data Committed"
except:
	print "Error : The database is being rolled back"
	db.rollback()
