<!DOCTYPE html>
<!--
Author : Kunchala Anil, Mohan Sir
Email : anilkunchalaece@gmail.com
Date : 2 july 2016

This code receives the Data From MySQl and Displays it as Webpage
-->
<html>
<head>
<title> Sensor Data </title>
</head>

<body>
<h2> Sensor Data From 3 slaves</h2>

<table>
<tr>
	<td>Device Id</td>
	<td>Time Stamp</td>
	<td>Sensor Type</td>
	<td>Sensor Value</td>
</tr>

</table>
<footer>
  <p>Done by: Kunchala Anil</p>
  <p>Email : anilkunchalaece@gmail.com</p>
</footer>
</body>
</html>

<?php
$serverName = "localhost";
$userName = "root";
$password = "raspberry";
$db = "sensorData";

//Create Connection
$conn = new mysqli($serverName,$userName,$password,$db);
if($conn ->connect_error){
	die("Connection Failed: ".$conn->connect_error);
	}
echo "Connected successfully";
$retval = mysqli_query($conn,"SELECT * FROM sensorDataTable");

if(!$retval){
	die('Could not get Data : '.mysqli_error());
}

while($row = mysqli_fetch_assoc($retval)){
echo "Device id :{$row['Device Id']}<br>".
	"Time Stamp :{$row['Time Stamp']}<br>".
	"Sensor Type :{$row['Sensor Type']}<br>".
	"Sensor Value.{$row['Sensor Value']}<br>".
	"--------------------------------------<br>";
}

echo "Fetched Data Sucessfully";
?>

