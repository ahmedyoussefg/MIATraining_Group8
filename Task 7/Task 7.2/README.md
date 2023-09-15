# PID Control Code

Below is the code for implementing a PID control system in Arduino. This code uses a custom PID library (likely defined in "pid_control.h") to control a system parameter, possibly a flow rate.

```cpp
#include "pid_control.h"

// Defining the current value for the flow rate and target flow rate 
// This should be edited so that this variable receives its input from the flow meter sensor 
double current_val = 0;
double target_val = 90;

// Creating an instance of PID Class
/*The K Parameters may need to be tuned */
PID pid_system(3, 10, 2, 0.5);

void setup() {
  Serial.begin(9600);
}

void loop() {
  current_val = pid_system.pid_control(current_val, target_val);
  Serial.println(current_val);
  delay(pid_system.getDelay());
}
```

## Code Explanation

- The code includes the "pid_control.h" header, which likely contains the PID class definition and related functions.

- It initializes two double variables: `current_val` (current system parameter value) and `target_val` (desired target value).

- An instance of the `PID` class named `pid_system` is created with specified PID controller parameters.

- In the `setup()` function, serial communication is initialized at a baud rate of 9600.

- The `loop()` function continuously performs the following:

  - Calculates the control output using the PID controller and updates `current_val`.

  - Sends `current_val` to the serial port for monitoring.

  - Introduces a delay based on the control loop's timing.

This code effectively implements a PID control loop, where the PID controller attempts to make `current_val` match `target_val`. You should adjust the PID parameters (Proportional, Integral, Derivative gains, and delay) to achieve the desired control behavior for your specific application.

# Class PID

[**Class List**](annotated.md) **>** [**PID**](classPID.md)

```cpp
#include <pid_control.h>
```

## Public Attributes

| Type | Name |
| ---: | :--- |
| double | [**derivative_term**](classPID.md#variable-derivative-term)  |
| double | [**error**](classPID.md#variable-error)  |
| double | [**integral_term**](classPID.md#variable-integral-term)  |
| double | [**previous_error**](classPID.md#variable-previous-error)  |
| double | [**proportional_term**](classPID.md#variable-proportional-term)  |

## Public Functions

| Type | Name |
| ---: | :--- |
| void | [**PID**](classPID.md#function-pid-1-2) ()  |
| void | [**PID**](classPID.md#function-pid-2-2)  |
| void | [**changeDelay**](classPID.md#function-changedelay)  |
| void | [**changeKd**](classPID.md#function-changekd)  |
| void | [**changeKi**](classPID.md#function-changeki)  |
| void | [**changeKp**](classPID.md#function-changekp)  |
| double | [**getDelay**](classPID.md#function-getdelay) ()  |
| double | [**getKd**](classPID.md#function-getkd) ()  |
| double | [**getKi**](classPID.md#function-getki) ()  |
| double | [**getKp**](classPID.md#function-getkp) ()  |
| double | [**pid_control**](classPID.md#function-pid-control)  |

## Public Attributes Documentation

### <a href="#variable-derivative-term" id="variable-derivative-term">variable derivative\_term </a>

```cpp
double PID::derivative_term;
```

### <a href="#variable-error" id="variable-error">variable error </a>

```cpp
double PID::error;
```

### <a href="#variable-integral-term" id="variable-integral-term">variable integral\_term </a>

```cpp
double PID::integral_term;
```

### <a href="#variable-previous-error" id="variable-previous-error">variable previous\_error </a>

```cpp
double PID::previous_error;
```

### <a href="#variable-proportional-term" id="variable-proportional-term">variable proportional\_term </a>

```cpp
double PID::proportional_term;
```

## Public Functions Documentation

### function PID [1/2]

### function PID [2/2]

### function changeDelay

### function changeKd

### function changeKi

### function changeKp

### function getDelay

### function getKd

### function getKi

### function getKp

### function pid_control

------------------------------
The documentation for this class was generated from the following file `src/pid_control.h`
