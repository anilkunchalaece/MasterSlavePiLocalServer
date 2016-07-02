# MasterSlavePiLocalServer
Arduino Master Slave using I2C and Posting the Data To the Local Server Running On Apache2 using mySql and PHP
<br><b>Done by : Kunchala Anil</b> </br>
<br>Email : anilkunchalaece@gmail.com</br>
<br>Date : July 2 2016</br>

1.To Install Apache2 in Raspberry Pi use the Command ;
  <br><i> sudo apt-get install apache2 php5 libapache2-mod-php5 </i></br>
2.After Finished Installing Use the Following Command to Restart the apache2 Server
  <br><i> sudo service apache2 restart </i></br>

3.After Restarting Check your Pi Ip Configuration with Command
  <br><i> ifconfig </i></br>

4.Enter the ipNumber in the Web browser in locla lan. you can see Sample Webpage as 
  <br><b>  It Works</b></br>
    
You can Edit the source file Location using
    <br><i> sudo nano /var/www/html/index.html </i></br>
note : You need to Change the Above file before Using It

5.Installing Php5 In Raspberry Pi : use the following command to install the Php
  <br><i> sudo apt-get install php5 libapache2-mod-php5 -y </i></br>
  
6.Installing My Sql on Raspberry Pi : Use the Following Command to Install The mySql
  <br><i>sudo apt-get install mysql-server python-mysqldb </i></br>
  This will install the mysql server and Python MySQLdb Module Also
  
7.Installing Php My Admin  : use the following Command to Install the Phpmyadmin
  <br><i> sudo apt-get install phpmyadmin </i></br>
  
8.Configure Apache2 to Work with Php My Admin
  <br><i> nano /etc/apache2/apache2.conf </i></br>
  <p> naviagate to the Bottom of the File and add the Following Line
      <br> <i> Include /etc/phpmyadmin/apache.conf </i></br>
      
9.restart the apache2 
    <br><i>/etc/init.d/apache2 restart</i></br>


    








Files Description

MasterCodeV3.ino: This is a Arduino Sketch for Master Which Receives the Data From 3 slaves via I2C and send the Data to the Raspberry Pi via UART

SlaveACodeV3.ino: This is a Arduino Sketch for SlaveA which reads the Data from Sensor And sent it to the Master Via I2C. In this Code I Used Potentiometer as a sensor. It is Connected to the pin A0.

SlaveBCodeV3.ino: This is a Arduino Sketch for SlaveB which reads the Data from Sensor And sent it to the Master Via I2C. In this Code I Used Potentiometer as a sensor. It is Connected to the pin A0.

SlaveCCodeV3.ino: This is a Arduino Sketch for SlaveC which reads the Data from Sensor And sent it to the Master Via I2C. In this Code I Used Potentiometer as a sensor. It is Connected to the pin A0.

csvWriter.py: This is a Python Code runs in the Raspberry pi and Receives the Code from Arduino Master Via UART and Writes it into the CSV File for Storing Purpose.

mysqlWriter.py: This is a Python Code runs in the Raspberry Pi and Receives the Code from Arduino Master via UART and Sends the Values to the mySQLdb on Apache2 server Running On raspberry Pi 

sensorData.php: This is a Php code to Receive the Data From mySQl Datatbase from server and Displays it on the Webpage

sensorDataTb.php: This is a Php Code to Receive the Data From mySQL Database from server and Displays it on the Webpage in Tables

mysqlEx.py: This is a python Code to check connection to the mysql Database

mysqlBug.py: Code is a improvisation for the mysqlEx.py

