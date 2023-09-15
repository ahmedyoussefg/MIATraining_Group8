# Motor Control Code

This Markdown file documents the Arduino code for controlling a motor's direction and speed using Cytron Driver, potentiometer and exponential smoothing.

- You will find attached another version of the code using Cytron Driver Library.

## Code Description

The code controls a motor's direction and speed based on the input from a potentiometer. It uses exponential smoothing to filter the potentiometer's values for smoother motor control.

### Pin Definitions

```cpp
#define MotorDirection 8
#define MotorSpeed 9
#define PotPin A0
```

- `MotorDirection`: Pin used to control the motor's direction.
- `MotorSpeed`: PWM pin used to control the motor's speed.
- `PotPin`: Analog pin to read the potentiometer's value.

### Variables

```cpp
int SpeedVal = 0;
float smoothingFactor = 0.1;
float filteredSpeed = 0.0;
```

- `SpeedVal`: Stores the current potentiometer reading.
- `smoothingFactor`: Adjust this value for smoothing the potentiometer readings.
- `filteredSpeed`: Stores the filtered motor speed value.

### Setup Function

```cpp
void setup() {
  pinMode(MotorDirection, OUTPUT);
  pinMode(MotorSpeed, OUTPUT);
  Serial.begin(9600);
}
```

- Configures the motor control pins as outputs.
- Initializes serial communication for debugging.

### Loop Function

```cpp
void loop() {
  SpeedVal = analogRead(PotPin);

  filteredSpeed = (1.0 - smoothingFactor) * filteredSpeed + smoothingFactor * SpeedVal;

  if (filteredSpeed > 542) {
    digitalWrite(MotorDirection, LOW);
    filteredSpeed = map(filteredSpeed, 542, 1024, 0, 255);
    analogWrite(MotorSpeed, filteredSpeed);
  }
  else if (filteredSpeed < 482) {
    digitalWrite(MotorDirection, HIGH);
    filteredSpeed = map(filteredSpeed, 482, 0, 0, 255);
    analogWrite(MotorSpeed, filteredSpeed);
  }

  Serial.print("Motor Speed = ");
  Serial.println(filteredSpeed);
}
```

- Reads the potentiometer value and applies exponential smoothing.
- Adjusts motor direction and speed based on the filtered value.
- Prints the filtered motor speed to the serial monitor.

## Usage

Upload this code to your Arduino board, and it will control the motor's direction and speed based on the potentiometer input. Adjust the `smoothingFactor` variable to fine-tune the smoothing effect as needed for your application.

## Q: Does this motor suitable for this application?

## A: 
- No this motor isn't suitable for this application because brushes and their lubricant will almost certainly contaminate your vacuum, and because if the vacuum is high enough the brushes will vacuum-weld to the commutator (unless you use graphite brushes, in which case the dust will really contaminate your vacuum).
- Opting for a brushless DC (BLDC) motor is a superior choice, offering higher efficiency, precise control, and greater reliability compared to traditional brushed motors. BLDC motors excel in applications requiring energy efficiency, accurate speed control, and reduced maintenance.
