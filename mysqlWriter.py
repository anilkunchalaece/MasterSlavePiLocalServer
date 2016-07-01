#!/usr/bin/python
#python location
# Author :Kunchala Anil
# Email : anilkunchalaece@gmail.com
# Date : july 1 2016
# This is the Python Code to Receive the Data From Arduino Master (Which is Getting Data From 3 other Slaves) via UART and Post it
# To the Local MySQLdb Database which is installed in the Raspberry Pi along with apache2 server and phpmyadmin
# it uses python Regular Expressions to Parse Data which is received via UART in format ex: A1234 where 'A' is slave identifier and 1234 is Sensor Value 
# I created a SQl Database named sensorData and with in it A Table Named sensorDataTable with Fields named
# `Device Id`,`Time Stamp`,`Sensor Type`,`Sensor value`

import serial # for Serial
import re #Regular Expression for Parsing the Data
import datetime #import the Date and Time Module to Get the Time
import MySQLdb #import the python MySQLdb library

#This Function is Called when the Data is received from Arduino Via USB. It process the Data and Store it In DataBase
def processData(data): 
	out = re.findall(r'([A-Z])(\d+)',data) #This Functions returns the list of Tuples with the Parsed Data
	#We only Post the Data If 'out' Variable is not Null. without this try and except the Python Throws Index Out of Boundaries Error
	try:
		if  out[0][0]:
			deviceId = str(out[0][0]) # the first tuple element in first list is Device Id
			sensorValue = out[0][1] #  the second tuple element in the first list is Sensor Value
        		timeStamp = datetime.datetime.now() #Get the Present Time
			timeStamp = str(timeStamp) #Convert the Datetime Object into String
			#this try and except used avoid database connection Errors
			try:
				#Insert the Data into Table named sensorDataTable in sensorData Database
				#We need to Pass the %s(string) as Argument for Integer also
				#please see : http://stackoverflow.com/questions/5785154/python-mysqldb-issues-typeerror-d-format-a-number-is-required-not-str
				curs.execute(""" INSERT INTO sensorData.sensorDataTable
					values(%s,%s,%s,%s)""",(deviceId,timeStamp,1,sensorValue))
				#Commit the Data
				db.commit()
				print 'Data Commited'
			except:
				print "Error : the DataBase is Being Rolled Back"
				db.rollback()
			
	except IndexError:
		#if we Didnt received the Correct Data Pass
		pass
	#return is Optional
	return

ser = serial.Serial('/dev/ttyACM0') #open the serial Connection between pi and Arduino
db = MySQLdb.connect("localhost","root","raspberry","sensorData") #Connect to the DataBase

curs = db.cursor() # open Cursor which is used to pass MySQLdb Queries

global counter # counter variable is used to keep track of No of Values Written into the DataBase
counter = 0;
#Infinite Loop
while True:
	if(ser.inWaiting() > 3) : #If Serial Buffer has More than 3 Bytes
		global counter # we need to reinitalize(?) the global Keyword in Functions 
		data = ser.readline() # read a Line of Data from Serial Buffer 
		processData(data) # Call the Function to Read the Data
		counter=counter+1 # Increment the Counter Value
		print 'count',counter  # Print the Counter Value
