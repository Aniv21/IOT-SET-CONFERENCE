// defines pins numbers
const int trigPin = 8;
const int echoPin = 9;
float height = 30;
// defines variables
long duration;
float distance;
void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}
float percentFull;
float GarbageValue() {
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10000000);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10000000);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance= duration*0.034/2;
  percentFull = ((height - distance)/height)*100;
  return percentFull; 
  
}

void loop() {
 
  /*// Clears the trigPin
  for(int i =0;i<100; i++) {
    delay(1);
  }*/

  unsigned int AnalogValue;
  AnalogValue = analogRead(A0);

  if(AnalogValue>700) {
    
    percentFull = GarbageValue();

  if(percentFull<0) {
    while(percentFull<0) {
        //Serial.println("Please Adjust the Ultrasonic Sensor!");
        percentFull = GarbageValue();
      }
  }
  if(percentFull > 50 && percentFull < 75) {
      //Serial.println("Alert ! The Dustbin  half filled ! Please Dump the Garbage"); 
  }

  int destination = random()%6;
  // Prints the distance on the Serial Monitor
  Serial.print("! The Grabage Bin is ");
  Serial.print(percentFull);
  Serial.print(" % full -");
  Serial.println(destination);  
  } else {
      Serial.println("There is no change in Garbage Content");
  }
  delay(5000);
  
}
