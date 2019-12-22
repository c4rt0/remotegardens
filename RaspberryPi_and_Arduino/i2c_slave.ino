#include <Wire.h>
 
#define SLAVE_ADDRESS 0x08

#define SensorPin 0            //pH meter Analog output to Arduino Analog Input 0
#define Offset 0.00            //deviation compensate

unsigned long int avgValue;     //Store the average value of the sensor feedback
#define FLOATS_SENT 1 
float data[FLOATS_SENT];
float phValue;
// Use the offset value to select a function
void sendData(){
  uint8_t buf[32]; // buffer in which to build block.*/
  uint8_t len=0;
  memmove(&buf[len],(uint8_t*)&phValue,sizeof(phValue));
  len += sizeof(phValue); 
  Wire.write(buf,len);
  Wire.write((byte*) &data, FLOATS_SENT*sizeof(float));
 
}

// Counter function
int PhSensor() {
   int buf[10];                //buffer for read analog
  for(int i=0;i<10;i++)       //Get 10 sample value from the sensor for smooth the value
  {
    buf[i]=analogRead(SensorPin);
    delay(100);
  }
  for(int i=0;i<9;i++)        //sort the analog from small to large
  {
    for(int j=i+1;j<10;j++)
    {
      if(buf[i]>buf[j])
      {
        int temp=buf[i];
        buf[i]=buf[j];
        buf[j]=temp;
      }
    }
  }
  avgValue=0;
  for(int i=2;i<8;i++)                      //take the average value of 6 center sample
    avgValue+=buf[i];
  phValue=(float)avgValue*5.0/1024/6;       //convert the analog into millivolt
  phValue=3.5*phValue+Offset;               //convert the millivolt into pH value
  Serial.print("    pH:"); 
  Serial.print(phValue,2);
  Serial.println(" ");
  return phValue;

  
 
}
 
 
void setup(){
 
  Serial.begin(9600); // start serial for output
  Wire.begin(SLAVE_ADDRESS);
  Wire.onRequest(sendData);
  Serial.println("I2C Ready!");
}
 
 
void loop(){

 data[0] = PhSensor(); 
 delay(500);
}
