// These constants won't change. They're used to give names to the pins used:
const int breakerInPin = A0;  // Analog input pin that the potentiometer is attached to
const int gyroInPin = A3;  // Analog input pin that the potentiometer is attached to
const int distanceInPin = A1;  // Analog input pin that the potentiometer is attached to


int breakerValue = 0;
int gyroValue = 0;
//int distanceValue = 0;
bool squatState = false;
bool pushupState = false;

//distance values
#define trigPin A2
#define echoPin A1
int mode = 1;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop() {
   long duration, distance;
  
  delay(1);
  if (true) {
    breakerValue = analogRead(breakerInPin);
    //Serial.println(breakerValue);
    if (breakerValue <= 500) {
      
    }

    if ((pushupState == false) and (breakerValue > 500)) {
      pushupState = true;
      
      
      delay(600);
    } if ((pushupState == true) and (breakerValue <500)){
      pushupState = false;
      Serial.println("PushUp");
      
    }
    
    //Serial.println(breakerValue);
  }
  if (true){
    
    //digitalWrite(trigPin, LOW);
    //delayMicroseconds(2);
    //digitalWrite(trigPin, HIGH);
    //delayMicroseconds(10);
    //digitalWrite(trigPin, LOW);
    //duration = pulseIn(echoPin, HIGH);
    //distance = (duration/2) / 29.1;

    //600 200 dead band
        distance = analogRead(distanceInPin);
    if ((squatState == false) and (distance < 200)) {
      squatState = true;
      
      
    } if ((squatState == true) and (distance >600)){
      squatState = false;
      Serial.println("Squat");
      
    }
    

    //Serial.println(distance);


  if (mode == 3) {
    
  }
    //if button pressed then rotate mode
  }
}
