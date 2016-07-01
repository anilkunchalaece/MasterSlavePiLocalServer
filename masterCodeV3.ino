/*
* Author : Kunchala Anil
* Email : anilkunchalaece@gmail.com
* Date : july 1 2016
* This is a Master Code for I2C Master which Receives the Data from 3 I2C Arduino Slaves and Send them to Raspberry Pi Via UART
*Bug in the Code : I2C Hangs If One Of Slaves Powered Down
* Check the Discussion Om : http://forum.arduino.cc/index.php?topic=409677.new#new
*/

//Include the Wire library
#include<Wire.h>

//Define the Slave Addresses
#define slaveA 8
#define slaveB 9
#define slaveC 10

//Variale to Hold the Received byte Length From I2C Slaves
byte byteLength = 2;
//Variable to Check Whether data is Received Or Not
boolean chRead = false;
//variable to hold the Received Serial Data
char ch;
unsigned long int interval = 10; // Duration for Requesting the Data
unsigned long int prevMillis = 0;
unsigned long int newMillis;

void setup() {
  Wire.begin();//Address is Optional For Master
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
     ch = Serial.read();
    chRead = true;
  }

  if(chRead){
    switch(ch){
      case 'a':
      requestSlaveA();
      break;

      case 'b':
      requestSlaveB();
      break;

      case 'c':
      requestSlaveC();
      break;

      case 'i':
      changeInterval();
      break;

      default:
      Serial.println("Please check the Command");
      
    }
    chRead = false;
  }

  newMillis = millis();
  if(newMillis - prevMillis >= interval*1000){
    prevMillis = newMillis;
    requestSlaveA();
    delay(100);
    requestSlaveB();
    delay(100);
    requestSlaveC();
  }

}

void requestSlaveA(){
  if(Wire.requestFrom(slaveA,byteLength)){
    Serial.print('A');
    Serial.println(getData());
  }else{
    Serial.println("EA");
  }
}


void requestSlaveB(){
  if(Wire.requestFrom(slaveB,byteLength)){
    Serial.print('B');
    Serial.println(getData());
  }else{
    Serial.println("EB");
  }
}

void requestSlaveC(){
  if(Wire.requestFrom(slaveC,byteLength)){
    Serial.print('C');
    Serial.println(getData());
  }else{
    Serial.println("EC");
  }
}


int getData(){
  int receivedValue  = Wire.read() << 8;
    receivedValue |= Wire.read();
    return receivedValue;
 }


void changeInterval(){
  Serial.println("Please enter the New Duration In Seconds");
  while(!Serial.available())
  {
    //Wait until User Responds
  }
  interval = Serial.parseInt();
  if(interval){
    Serial.print("The New Interval is -->\t");
    Serial.print(interval);
    Serial.println("  Seconds");
    
  }else{
    Serial.println("PLease Enter the Valid Number");
    changeInterval();
  }
}

