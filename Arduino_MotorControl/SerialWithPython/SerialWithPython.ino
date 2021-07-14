#include <Servo.h>
int a;
int SensorVal=0;
void setup() {
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(7,INPUT);
}

void loop() {
   if(Serial.available()>0)
  {
    a=Serial.read();
    if (a==1){
    digitalWrite(2, LOW);       
    analogWrite(3, 15);
   
    
    }
    else if (a==2){
    digitalWrite(2, HIGH);       
    analogWrite(3, 15);        
    //delay(3000);     
    }
    else{
    digitalWrite(2, HIGH);       
    analogWrite(3, 0);        
    //delay(3000)
    }
  
  }

}
