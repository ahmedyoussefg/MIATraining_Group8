import math

# Wheel radius
r = 20  # cm

# Wheel angles in radians
theta1 = 0  # Wheel 1
theta2 = math.radians(120)  # Wheel 2
theta3 = math.radians(240)  # Wheel 3

# Constants for the PID controller
KP = 0.1  # Proportional gain
KI = 0.01  # Integral gain
KD = 0.02  # Derivative gain

# Target position
target_x = 100  # Target x-coordinate in cm
target_y = 50   # Target y-coordinate in cm

# Current position (initially assumed to be at the origin)
current_x = 0   # Current x-coordinate in cm
current_y = 0   # Current y-coordinate in cm

# Initialize PID control variables
error_sum = 0
prev_error = 0

# Maximum and minimum angular velocities for motors (radians/s)
max_angular_velocity = 1.0  # Adjust as needed
min_angular_velocity = -1.0  # Adjust as needed

def calculate_motor_angular_velocity(Vx, Vy, omega):
    # Calculate the linear velocity of each wheel
    V1 = Vx * math.cos(theta1) + Vy * math.sin(theta1) + r * omega
    V2 = Vx * math.cos(theta2) + Vy * math.sin(theta2) + r * omega
    V3 = Vx * math.cos(theta3) + Vy * math.sin(theta3) + r * omega

    # Calculate the angular velocity of each motor
    omega1 = V1 / r
    omega2 = V2 / r
    omega3 = V3 / r

    # Ensure that the angular velocities are within limits
    omega1 = max(min_angular_velocity, min(max_angular_velocity, omega1))
    omega2 = max(min_angular_velocity, min(max_angular_velocity, omega2))
    omega3 = max(min_angular_velocity, min(max_angular_velocity, omega3))

    return omega1, omega2, omega3

def calculate_pid_instruction(target_x, target_y, current_x, current_y):
    global error_sum  # Declare error_sum as a global variable
    global prev_error  # Declare prev_error as a global variable

    # Calculate the position error
    error_x = target_x - current_x
    error_y = target_y - current_y

    # Calculate the total position error
    total_error = math.sqrt(error_x**2 + error_y**2)

    # Calculate the PID terms
    P = KP * total_error
    I = KI * (error_sum + total_error)
    D = KD * (total_error - prev_error)

    # Calculate the PID instruction (adjust motor angular velocities)
    instruction = P + I + D

    # Update PID control variables
    error_sum += total_error
    prev_error = total_error

    return instruction

# Simulation loop
for _ in range(100):
    instruction = calculate_pid_instruction(target_x, target_y, current_x, current_y)

    # Calculate motor angular velocities
    omega1, omega2, omega3 = calculate_motor_angular_velocity(0, 0, instruction)

    # Update the current position based on the motor angular velocities
    current_x += r * (math.cos(theta1) * omega1 + math.cos(theta2) * omega2 + math.cos(theta3) * omega3)
    current_y += r * (math.sin(theta1) * omega1 + math.sin(theta2) * omega2 + math.sin(theta3) * omega3)

    print(f"Instruction: {instruction}, Current Position: ({current_x}, {current_y})")

# Stop the motors when the target position is reached
omega1 = 0
omega2 = 0
omega3 = 0
