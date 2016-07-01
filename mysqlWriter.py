#!/usr/bin/python
#python location

import serial # for Serial
import re #Regular Expression for Parsing the Data
import datetime
import MySQLdb #import the python MySQLdb library

def processData(data): 
	out = re.findall(r'([A-Z])(\d+)',data)
	try:
		if  out[0][0]:
			deviceId = str(out[0][0])
			sensorValue = out[0][1]
        		timeStamp = datetime.datetime.now()
			timeStamp = str(timeStamp)
			try:
				curs.execute(""" INSERT INTO sensorData.sensorDataTable
					values(%s,%s,%s,%s)""",(deviceId,timeStamp,1,sensorValue))
				db.commit()
				print 'Data Commited'
			except:
				print "Error : the DataBase is Being Rolled Back"
				db.rollback()
			
	except IndexError:
		pass
	return

ser = serial.Serial('/dev/ttyACM0') #open the serial Connection between pi and Arduino
db = MySQLdb.connect("localhost","root","raspberry","sensorData") #Connect to the DataBase

curs = db.cursor()


global counter
counter = 0;
while True:
	if(ser.inWaiting() > 3) :
		global counter
		data = ser.readline()
		processData(data)
		counter=counter+1
		print 'count',counter 
