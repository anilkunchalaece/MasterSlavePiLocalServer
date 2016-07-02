<!DOCTYPE html>

<!DOCTYPE html>
<!--
Author : Kunchala Anil, Mohan Sir
Email : anilkunchalaece@gmail.com
Date : 2 july 2016

This code receives the Data From MySQl and Displays it as Webpage as a Table
-->

<html>
<head>
<title> Sensor Data </title>
</head>

<body>
<h2> Sensor Data From 3 slaves</h2>

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
echo "<table style='border : 1px solid black'>";

echo "<tr>
	<td style='border : 1px solid black'>Device Id</td>
	<td style='border : 1px solid black'>Time Stamp</td>
	<td style='border : 1px solid black'>Sensor Type</td>
	<td style='border : 1px solid black'>Sensor Value</td>
</tr>";

while($row = mysqli_fetch_assoc($retval)){
 echo "<tr >
	<td style='border : 1px solid black'>{$row['Device Id']}</td>
	<td style='border : 1px solid black'>{$row['Time Stamp']}</td>
	<td style='border : 1px solid black'>{$row['Sensor Type']}</td>
	<td style='border : 1px solid black'>{$row['Sensor Value']}</td>
	</tr>";
}
echo "</table>";

echo "Fetched Data Sucessfully";
?>

<footer>
  <p>Done by: Kunchala Anil</p>
  <p>Email : anilkunchalaece@gmail.com</p>
</footer>
</body>
</html>
