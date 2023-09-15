# Kinematic Model for Three-Wheel Configuration

In this kinematic model, we have a vehicle with three wheels, all connected to the center of an imaginary circle with a radius of 20 cm. Each wheel is adjusted to a specific angle as follows:

1. Wheel 1 is adjusted at θ1 = 0 degrees.
2. Wheel 2 is adjusted at θ2 = 120 degrees.
3. Wheel 3 is adjusted at θ3 = 240 degrees.

## Equations for Wheel Positions

To calculate the positions of the wheels on the circumference of the imaginary circle, we use the following equations:

- Wheel 1: (x1, y1) = (20 * cos(0), 20 * sin(0)) = (20, 0) cm
- Wheel 2: (x2, y2) = (20 * cos(120), 20 * sin(120)) = (-10, 17.32) cm
- Wheel 3: (x3, y3) = (20 * cos(240), 20 * sin(240)) = (-10, -17.32) cm

## Calculation of Vehicle Center Position

The position of the vehicle's center can be calculated as the centroid of the three wheel positions:

- x = (x1 + x2 + x3) / 3 = (20 - 10 - 10) / 3 = 0 cm
- y = (y1 + y2 + y3) / 3 = (0 + 17.32 - 17.32) / 3 = 0 cm

## Calculation of Heading Angle (θ)

The heading angle (θ) of the vehicle can be calculated as the angle between the line connecting the center of the circle to the center of the vehicle and the positive x-axis:

- θ = atan2(y, x) = atan2(0, 0)

Note: The heading angle (θ) is undefined in this case because the vehicle is at the origin, and division by zero occurs. This means that the vehicle does not have a unique heading in this configuration.

