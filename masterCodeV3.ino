#include<Wire.h>

#define slaveA 8
#define slaveB 9
#define slaveC 10

#define byteLength 2
int noOfValues = 0;
boolean chRead = false;
char ch;
unsigned long int interval = 10; // Duration for Requesting the Data
unsigned long int prevMillis = 0;
unsigned long int newMillis;

void setup() {
  Wire.begin();//Address is Optional For Master
  Serial.begin(9600);
//  Serial.println("Please enter --> a to read the data from Slave 1 ");
//  Serial.println("Pleae enter -->  b to read the data from slave 2 ");
//  Serial.println("Please enter --> c to read the data from slave 3");
//  Serial.println("Please enter --> i to Change the Duration (Default Duaration is 10 Seconds)");
  
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
    noOfValues++;
    //Serial.print("The No Of vaues Received is -->\t");
    //Serial.println(noOfValues);
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

