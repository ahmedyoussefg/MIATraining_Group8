#include "CytronMotorDriver.h"

/* Configure the motor driver */
CytronMD motor(PWM_DIR, 3, 4);  // PWM = Pin 3, DIR = Pin 4.

/* Exponential smoothing parameters */
float smoothingFactor = 0.1;  // Adjust this value as needed for your application
int targetSpeed = 0;
int currentSpeed = 0;

void setup() {
  /* Initialize the motor driver here if necessary */
  motor.begin();
  motor.setSpeed(0); // Start with the motor stopped
}

void loop() {
  /* Gradually change the target speed */
  targetSpeed = map(analogRead(A0), 0, 1023, 0, 255);  // Read from a potentiometer, adjust as needed

  /* Calculate the smoothed speed using exponential smoothing */
  currentSpeed = (1.0 - smoothingFactor) * currentSpeed + smoothingFactor * targetSpeed;

  motor.setSpeed(currentSpeed);

  /* Add a delay to control the rate of change */
  delay(100);
}
