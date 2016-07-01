#include<Wire.h>
#define slaveA 8
#define AnalogInputPin A0

void setup() {
   Wire.begin(slaveA);
   Wire.onRequest(requestCallback);
}

void loop() {
  // Do nothing
}

void requestCallback(){
 int input = analogRead(AnalogInputPin);
 // To send multiple bytes from the slave,
 // you have to fill your own buffer and send it all at once.
  uint8_t buffer[2];
  buffer[0] = input >> 8;
  buffer[1] = input & 0xff;
  Wire.write(buffer, 2);
}

