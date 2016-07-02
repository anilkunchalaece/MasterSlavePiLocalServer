import serial # for Serial
import re #Regular Expression for Parsing the Data
import datetime
import csv #for Writing the CSV Files
#datetime.now().strftime('%Y-%m-%d %H:%m')
#out= [(0,0)] # Dummy Variable for Storing the Data

def processData(data): 
	#print data
	#print 'i am in Process data function' 
	out = re.findall(r'([A-Z])(\d+)',data)
	#print out
	try:
		if  out[0][0]:
			outputFile = open('output.csv','a')# "a" Mode for Appending The Previous Values
			outputWriter = csv.writer(outputFile)
			deviceId = str(out[0][0])
			sensorValue = str(out[0][1])
        		timeStamp = datetime.datetime.now()
			timeStamp = str(timeStamp)
			outputWriter.writerow([deviceId,timeStamp,1,sensorValue])
			outputFile.close()
			#print 'Data Written to the File'
	except IndexError:
		pass
	return

ser = serial.Serial('/dev/ttyACM2') #open the serial Connection between pi and Arduino
outputFile = open('output.csv','w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Device ID','Time Stamp','Sensor Type','Sensor Value'])
outputFile.close()
global counter
counter = 0;
while True:
	if(ser.inWaiting() > 3) :
		global counter
		data = ser.readline()
		processData(data)
		counter=counter+1
		print 'count',counter 
