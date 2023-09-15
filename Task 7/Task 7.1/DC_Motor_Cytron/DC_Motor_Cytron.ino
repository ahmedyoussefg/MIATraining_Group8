/* Pins used to control direction and speed of the motor. Speed pin should be a PWM pin. */
#define MotorDirection 8
#define MotorSpeed 9
#define PotPin A0

int SpeedVal = 0;

/* Exponential smoothing parameters */
float smoothingFactor = 0.1;  // Adjust this value as needed for your application
float filteredSpeed = 0.0;

void setup() {
  /* Declaration for the pins used, both should be outputs. */
  pinMode(MotorDirection, OUTPUT);
  pinMode(MotorSpeed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  SpeedVal = analogRead(PotPin); // Read the position of the potentiometer

  /* Calculate the filtered speed using exponential smoothing */
  filteredSpeed = (1.0 - smoothingFactor) * filteredSpeed + smoothingFactor * SpeedVal;

  /* Makes the motor rotate in the clockwise direction. */
  if (filteredSpeed > 542) {
    digitalWrite(MotorDirection, LOW);
    filteredSpeed = map(filteredSpeed, 542, 1024, 0, 255);
    analogWrite(MotorSpeed, filteredSpeed);
  }
  
  /* Makes the motor rotate in the counter-clockwise direction. */
  else if (filteredSpeed < 482) {
    digitalWrite(MotorDirection, HIGH); 
    filteredSpeed = map(filteredSpeed, 482, 0, 0, 255);
    analogWrite(MotorSpeed, filteredSpeed);
  }
  
  Serial.print("Motor Speed = ");
  Serial.println(filteredSpeed);
}