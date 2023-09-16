import cv2
import numpy as np

# Load left and right stereo images
# repalce left/right_image.png with photos path
left_image = cv2.imread('left_image.png', cv2.IMREAD_GRAYSCALE)
right_image = cv2.imread('right_image.png', cv2.IMREAD_GRAYSCALE)

# Block matching parameters
block_size = 5  # Size of the matching window
max_disparity = 64  # Maximum allowed disparity

# Create a StereoSGBM object (Semi-Global Block Matching)
stereo = cv2.StereoSGBM_create(
    minDisparity=0,
    numDisparities=max_disparity,
    blockSize=block_size,
    P1=8 * 3 * block_size ** 2,
    P2=32 * 3 * block_size ** 2,
    disp12MaxDiff=1,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=32,
    mode=cv2.STEREO_SGBM_MODE_SGBM
)

# Compute the disparity map
disparity_map = stereo.compute(left_image, right_image)

# Normalize the disparity map for display
disparity_map = cv2.normalize(disparity_map, None, 0, 255, cv2.NORM_MINMAX)

# Display the disparity map
cv2.imshow('Disparity Map', disparity_map)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculate depth from the disparity map (assuming baseline and focal length are known)
baseline = 0.1  # Example baseline in meters
focal_length = 500  # Example focal length in pixels
depth_map = (baseline * focal_length) / (disparity_map + 1e-6)

# Display the depth map
cv2.imshow('Depth Map', depth_map)
cv2.waitKey(0)
cv2.destroyAllWindows()